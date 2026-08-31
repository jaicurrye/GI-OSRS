---
name: session-omega
description: End-of-campaign review and next-campaign design for the claude-dnd-skill. Use when a D&D campaign is ending or has ended and the player wants to review it, extract lessons into a DM behaviour contract, and design the theme, setting and characters for the next campaign. Triggers on "session omega", "campaign review", "campaign post-mortem", "end of campaign", "wrap up the campaign", "plan the next campaign", "campaign retrospective", or when a player finishing a long campaign asks what to do next.
---

# Session Omega

The ritual at the end of a campaign that manufactures the beginning of the next
one. Session Zero runs before the first session; Session Omega runs after the
last, and its output *is* the next Session Zero.

It exists because a long campaign is the only source of honest data about how a
player actually likes to play — and almost everyone throws that data away.

## Invocation

`/session-omega <stage> [campaign]` — or plain language ("let's do the campaign
review"). With no stage, run `status` and propose the next one.

Stages run in order, but each is independently invocable and independently
resumable. Never run more than one stage without checking in — these are long,
and the player decides when to continue.

| Stage | Purpose |
|---|---|
| `predict` | **Before the finale.** Capture predictions and hopes, sealed. |
| `review` | Cold interview. No file reads. Unanchored answers. |
| `evidence` | Targeted extraction, then reconcile record against memory. |
| `tooling` | Audit the plugin itself: health, usage, failures, config. |
| `chronicle` | *Optional.* Narrative keepsake, epilogues, DM reveals. |
| `contract` | Tiered DM behaviour contract + the three table dials. |
| `spec` | Taste profile → pre-filled constraint sheet the player overrides. |
| `world` | Setting skeleton: theme, central conflict, region, three truths. |
| `party` | Party architecture, then characters tied to world and each other. |
| `build` | Write the new campaign's files. `/dm:dnd load` works after this. |
| `audit` | Re-run at ~session 5 and ~15 of the new campaign. Test the contract. |

## Setup — do this first, every stage

`${CLAUDE_SKILL_DIR}` must expand to this skill's directory. If a command fails
with a path starting `/scripts/`, the variable is unset — substitute the real
path before continuing rather than retrying.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py roots
python ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py campaigns
# first run only — `status` exits with an error until this exists:
python ${CLAUDE_SKILL_DIR}/scripts/omega_state.py init <campaign> --new-campaign <new>
python ${CLAUDE_SKILL_DIR}/scripts/omega_state.py status <campaign>
```

`roots` reports the data root, and whether the dnd skill's `templates/` were
found — `build` needs them. If `dnd_skill_root` is null, ask the player where
the dnd skill is installed rather than guessing or writing files from memory.

**Record every answer as it is given**, not at the end of a stage:

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_state.py record <campaign> <stage> <key> --stdin <<'ANS'
<the player's answer, verbatim>
ANS
```

Verbatim. Do not summarise the player into their own review — a paraphrase made
at the moment of writing is a paraphrase you will later treat as evidence.

**Close every stage explicitly.** Recording answers moves a stage to `active`;
nothing moves it to `done` on its own, and `status.next` keeps returning the
first unfinished stage until you do:

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_state.py set <campaign> <stage> done
```

Read answers back with `dump <campaign> --stage <stage>`. Keys beginning
`sealed_` are withheld from `dump` and need `--key` to read — that is how
`predict` question 5 stays sealed until `spec`.

Outputs land in `<campaigns>/<campaign>/omega/` — `progress.json`, `review.md`,
`tooling.md`, `contract.md`, `spec.md`, `chronicle.md` — where `<campaign>` is
the campaign being reviewed. Structure each from the matching file in this
skill's `templates/`. The one file that must not stay there is the situational
contract: `build` copies it into the new campaign as `dm-contract.md`, because
that is where the pointer in `state.md` will look for it.

---

## Before you start

Two things, once, before `review`:

1. **Close the old campaign properly.** `/dm:dnd save` then `/dm:dnd end` on the
   finale. That is what writes the final `### DM Calibration` block, the last
   `## Recent Events`, and the closing `## Continuity Archive` entries — all of
   which `evidence` then reads. Reviewing before the campaign is ended reviews
   an incomplete record.
2. **Back up the campaign directory.** `cp -r <campaigns>/<campaign>
   <campaigns>/<campaign>.omega-backup-<date>`. Nothing here rewrites the old
   campaign, but a hundred sessions deserves a copy before a process starts
   touching the directory at all.

And name the new campaign before `build` — `omega_state.py init` takes
`--new-campaign`, and `build` will refuse to overwrite an existing directory.

---

## Stage: `predict`

Run **before the final session**, and only then. If the finale has already
happened, say so and skip — a prediction written after the fact is worthless,
and pretending otherwise poisons the comparison in `review`.

Ask five questions, record verbatim, and do not discuss the answers:

1. How do you think this campaign ends?
2. How do you *want* it to end — the same thing, or something you don't expect
   to get?
3. Which thread are you most afraid will be left dangling?
4. What would make the finale a disappointment, specifically?
5. When you imagine the next campaign, what image or premise do you keep
   drifting toward — and what are you most sick of?

Tell the player to answer fast and slightly carelessly. Over-deliberation
produces what a sophisticated player thinks they *should* predict, which is
worth nothing; a worse-considered honest answer is the useful one.

Record questions 1–4 under keys `q1`…`q4`, and **question 5 under the key
`sealed_q5_appetite`** — the `sealed_` prefix is what hides it from
`dump --stage predict`, so the seal is enforced by the tool rather than by
remembering. Read it at `spec` with
`dump <campaign> --stage predict --key sealed_q5_appetite`.

Questions 1–4 unseal at `evidence`. **Question 5 unseals at `spec`**, not
earlier — it is a snapshot of unprompted creative appetite taken before a
hundred sessions of retrospection reframe it, and reading it during the review
would let it steer the very findings it is supposed to be tested against.

Then stop. Do not offer opinions on the predictions, do not foreshadow, and do
not let the answers influence how the finale is run. This last rule is a
constraint on the DM more than the player: having just read what the player
hopes for and fears, running the finale straight becomes hard, and delivering
the hoped-for thing would write the answer key and then grade against it.

**Done when:** five answers recorded (q5 under `sealed_q5_appetite`), nothing discussed, stage set `done`.

---

## Stage: `review`

**Read no campaign files during this stage.** The whole point is an unanchored
account. `evidence` is where the record speaks.

Work through the dimensions in `reference/review-dimensions.md`. Cover all of
them; skip questions that clearly don't apply to this table.

### Posture: dig, and argue back

The player asked to be pushed. Three rules make that productive rather than
merely unpleasant:

1. **Vague answers get up to two follow-ups**, and the follow-up always demands
   a specific instance — a session, a scene, an NPC, a moment. "Combat got
   stale" is not a finding. "Combat got stale around session 60, when every
   fight became a resource-attrition problem I'd already solved" is a rule.
   After two attempts, record it as `impression, unverified` and move on;
   `evidence` will test it.
2. **Argue only from cited record.** You were the DM for this campaign. When
   the player's account contradicts something you can cite, say so and name the
   session or scene. Never argue from impression, and never argue to defend
   your own performance — argue because an inaccurate diagnosis produces a bad
   contract.
3. **The player gets the last word, always.** If they hold their position after
   you have made your case, the matter is settled in their favour for the
   purposes of the review — but record the disagreement:

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_state.py dispute <campaign> "<the claim>" \
  --dm "<what the record shows>" --player "<what they hold>"
```

Disputed items are not failures of the interview. They are the most interesting
thing it produces, and `contract` turns them into labelled experiments.

Watch for the failure this posture creates: a player who starts softening real
complaints to avoid the argument. If answers get shorter and more agreeable
after a disagreement, name it, drop the pushback for a few questions, and come
back to the softened answer later.

Write `omega/review.md` as you go.

**Done when:** all six dimensions in `reference/review-dimensions.md` have been covered, every answer is recorded verbatim, disputes are logged, `omega/review.md` is written, and the stage is set `done`. Do not close it with dimensions unasked.

---

## Stage: `evidence`

Now read. Targeted only — never sweep a 100-session log.

**Run one target at a time.** All six at once on a long campaign returns tens of
thousands of tokens in a single result, which costs more context than the
findings are worth.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py extract <campaign> --what calibration
# then arc, mortality, npcs, party, sessions — reading each before the next
```

`/dm:dnd save` keeps only the two most recent sessions in `session-log.md` and
appends everything older to `session-log-archive.md`, so the archive is where a
long campaign actually lives — the extractor searches both, plus `npcs-full.md`
where NPC detail is kept.

Every target reports whether its result is complete. `files_capped` names files
that hit the per-file limit; `stopped_by` is set when the whole target hit the
global count or byte ceiling, and `files_unsearched` then lists what was never
reached. Any of the three means you are looking at a partial result.

When that happens, **narrow before you widen** — search a single file
(`--what npcs` reads all of them, but the dnd skill's `campaign_search.py` takes
`--files archive` and does keyword AND-search; its path is in
`omega_paths.py roots`). Raising `--max-bytes` on a 100-session campaign is how
you lose the session to one tool result.

Start with `calibration`. If the table has used `/dm:dnd end`, this returns the
player's own per-session answers to *"what worked, and what would you adjust?"*
across the whole campaign — the single richest input to the contract, and
better evidence than the interview because it was written without hindsight.
Read them chronologically and look for **the note that recurs**: a complaint
made once is a mood, a complaint made in sessions 12, 40 and 81 is a rule.

Then, per target:

- `arc` — which beats completed, which were skipped, how often the arc was
  revised. Frequent revision means the arc wasn't tracking what the player
  actually pursued.
- `mortality` — deaths, downed characters, near-TPKs. Compare the real count
  against what the player said about stakes. A player who says "I was never in
  danger" and a log with four death saves disagree about something important.
- `npcs` — attitude shifts, betrayals, allies. Find NPCs who appeared once and
  vanished; ask whether they were dropped or resolved.
- `party` — roster changes, plus `character_timeline`: every character file
  with its mtime, oldest first. For this table specifically, the gap in that
  timeline dates when the two DM-run PCs were taken over. Confirm the date
  against the log before treating it as fact — a copied file carries a copy
  time — then reconstruct why.
- `sessions` — session headers. Look for gaps in the calendar (where momentum
  was lost) and clusters (where it was highest).

Also read `state.md → ## DM Style Notes` — the calibration patterns already
distilled during play. Some contract lines are already written; the question is
whether they worked.

### Reconciliation

Put the interview answers beside the record and produce three lists:

- **Confirmed** — memory and record agree. These become contract lines with the
  highest confidence.
- **Contradicted** — they disagree. Present each one plainly, with the citation,
  and let the player respond. Do not adjudicate; record the outcome.
- **Invisible** — in the record but absent from the interview. Things that
  happened that the player never mentioned. Often the most revealing category:
  a whole faction arc nobody remembers is a finding about what the table
  actually cares about.

Append all three to `omega/review.md`. If `predict` ran, unseal it here and
compare predictions against what the finale actually was.

**Done when:** every target has been extracted with no unexplained `files_capped`, the three reconciliation lists are written into `omega/review.md`, `predict` q1–q4 are unsealed and compared, and the stage is set `done`.

---

## Stage: `tooling`

A different axis from everything else here. `review` and `contract` ask whether
the DM played well; this asks whether the *machinery* served the table. After a
hundred sessions a campaign accumulates operational debt that is invisible
during play — sessions that start slowly, continuity that quietly degrades,
features that were there the whole time and never got used.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_health.py all <campaign>
```

**Read `reference/tooling.md` before interpreting the output.** It carries the
load-path model, what each measurement means, the five parts of the audit, and
the placement rules for anything new. Work all five parts; they inform each
other, and part 5 feeds `build`.

`load_path.per_session_est_tokens` in the report is the number this stage exists
to produce. What is and is not on that load path is not obvious and is easy to
get backwards — the reference states it; do not work from memory.

Write `omega/tooling.md` using `templates/tooling.md` as the structure. Its
config and extensions blocks are consumed by `build`.

**Done when:** `omega/tooling.md` exists with all five parts filled, the config
block is complete, and `omega_state.py set <campaign> tooling done` has run.

## Stage: `chronicle` *(optional)*

Skip on request; it costs a generation pass and produces nothing the next
campaign needs. It is for the player, not the process.

A narrative retelling — acts and turning points, the NPCs who mattered and what
became of them, the party's climb from 1 to 20, an epilogue for each character,
and the DM's reveals: the plots they never uncovered, the NPC whose motive was
never explained, what would have happened down the road not taken.

Write it as story, not analysis. Read from `## Continuity Archive` and
`session-log.md` for material. Output: `omega/chronicle.md`.

**Done when:** `omega/chronicle.md` is written, or the stage is set `skipped`.

---

## Stage: `contract`

See `reference/contract.md` for the full procedure, the dial mapping, and the
tests every candidate line must pass.

**First, read the upstream Standards.** One of those tests rejects any line that
merely restates a behaviour the dnd skill already mandates, and you cannot apply
it from memory. Read the `## What Makes a Great DM — Applied Standards` section of
`<dnd_skill_root>/SKILL.md` — the path comes from `omega_paths.py roots` —
before writing a single candidate.

In short: a **tiered** DM behaviour contract, sized by what the review actually
found rather than a fixed count.

- **Core** → `state.md → ## DM Style Notes` in the new campaign. Read at every
  `/dm:dnd load`, overrides default DM instincts. Every line here costs context
  for the life of the campaign, so it must earn its place.
- **Situational** → drafted in `omega/contract.md`, then **copied by `build`
  into the new campaign as `dm-contract.md`**. The pointer line in the new
  `state.md` names that file. Drafting it in the old campaign's `omega/` and
  pointing at it from the new one leaves a path that does not resolve — the
  exact unreachable-file failure this skill warns about.
- **Dials** → `state.md → ## Session Flags`: `difficulty`, `spotlight`,
  `pacing`. Set explicitly, with the review finding that justifies each.
- **Experiments** → disputed items, written with a success condition and a
  revert condition, resolved at `audit`.

**Done when:** the upstream Standards have been read, every core line carries a citation, the three dials have values and findings, disputes have become experiments with revert conditions, `omega/contract.md` is written, and the stage is set `done`.

---

## Stage: `spec`

See `reference/setting.md`.

Derive a taste profile from the review and the evidence — what the player
*engaged with*, which is not what they would say if asked cold. Then pre-fill
the constraint sheet, showing the proposed value and the finding behind it for
every field. The player confirms or overrides each one.

Never present a blank questionnaire. The work of this stage is doing the
inference so the player only has to react to it.

**If `predict` never ran**, say so plainly and skip the comparison below — ask
the appetite question now instead, and note in `spec.md` that the answer was
given after the review and is not independent of it.

Otherwise, **unseal question 5 from `predict` here**, and only after the taste
profile is written — the profile must be derived from evidence before the player's stated
appetite is allowed in the room. Then compare the two.

Where they agree, the constraint sheet writes itself. Where they disagree, say
so plainly and let the player decide; do not quietly resolve it in favour of the
evidence. Players are frequently sick of the thing they in fact loved, and drawn
to a thing they never once chose when it was available — both readings are real,
and which one should win is the player's call, not an inference.

Fixed for this table, already decided:

- Fresh world, no continuity with the old campaign.
- Designed for a long epic — with act-boundary exits so a stop at session 40 is
  an ending rather than an abandonment.
- Start at level 1, accelerated through tier 1 (a level every session or two
  until 5), so the zero-to-hero arc is real without the level-20-to-level-1
  whiplash.

Output: `omega/spec.md`.

**Done when:** the taste profile was written before q5 was unsealed, every constraint field has a player-confirmed value, and `omega/spec.md` is written. Set the stage `done`.

---

## Stage: `world`

Skeleton only — enough setting to make characters meaningful, and no more:
theme, central conflict, the region play starts in, and three truths about the
world. The rest is deliberately deferred until after `party`, so the world can
be shaped around the characters that actually got made.

The central conflict must be renewable: for a 100-session campaign it needs to
escalate for years without resolving, and factions need somewhere to go. Test
it by asking what this conflict looks like at session 80. If the answer is "the
same, but bigger", it isn't renewable.

**Done when:** theme, central conflict, starting region and three truths are written into `omega/spec.md`, and the conflict has passed the session-80 test. Set the stage `done`.

---

## Stage: `party`

**Party architecture first.** How many PCs, who runs which, whether DM-run
companions exist at all. This table ran 1+1 player / 2 DM and migrated to all
four player-run — the review must have established why before this stage
decides anything.

Then characters: each PC needs a tie to the central conflict, a tie to at least
one other PC, and something they want that the campaign can threaten.

Mechanical creation hands off to `/dm:dnd character new` — this skill produces
the narrative spec, not the stat block.

**Done when:** the party model is chosen with the review finding that justifies it, and every PC has all three ties. Set the stage `done`.

---

## Stage: `build`

Write the new campaign's files directly from the dnd skill's own templates.

**Do not run `/dm:dnd new`.** It auto-generates a world seed, factions and a
three-act arc, which would overwrite or fight everything `world` and `party`
produced.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py roots   # for templates_dir
```

Copy `state.md`, `world.md`, `npcs.md`, `session-log.md` from **the dnd skill's**
`templates/` (`templates_dir` in `omega_paths.py roots` — not this skill's
`templates/`, which holds Session Omega's own output shapes) into
`<campaigns>/<new-campaign>/`, then populate:

- `state.md` header: name, date, session count 0, and the **ruleset** line
  (`**Ruleset:** 2014` or `2024`) — a campaign without it triggers a migration
  prompt on first load.
- `## DM Style Notes` — the core contract. **Add this section**; the blank
  template does not include it, but `/dm:dnd load` reads it.
- `## Session Flags` — the three dials, plus `roll_mode` and `autosave` from
  the `tooling` config block.
- `## Campaign Arc` — the dynamic-arc YAML block, filled from `world`.
- `world.md` — **populate it fully**, not just `## Adventure Nodes`. It is read
  in full at every load, so placeholders cost the same as content and return
  nothing. Follow the template's own shape rather than inventing sections: it
  carries `## The Settlement`, `## The Nearby Threat` and `## The Mystery`, each
  with its own `### Three Truths` subsection, plus `## Factions` and the quest
  seeds. `spec`'s three world-truths are a different thing — distribute them
  into those three subsections, or add them under World Foundations; do not
  create a top-level `## Three Truths`, which the template does not have.
- `state.md → ## World State` — faction states, threat arc stage, in-world date.
  Standard 11 (Faction Moves) has nothing to operate on without these.
- `npcs.md` — the opening NPCs with a relationship web between them, the way
  `/dm:dnd new` would have seeded them.
- `characters/` — via `/dm:dnd character new`.
- Anything else the `tooling` config block calls for: initialize the
  relationship graph if the last campaign never had one, and write the archive
  compression cadence into `## DM Notes` so it happens without being
  remembered.
- `dm-contract.md` — copy the situational tier from `omega/contract.md` into
  the new campaign directory, and make the pointer line in `## DM Style Notes`
  name `dm-contract.md`. Verify the path resolves from the new campaign dir.
- The `tooling` extensions block: install what it calls for, and place each
  piece of custom content where that block assigned it.
- `## DM Notes` — the things that otherwise have no mechanism:
  - **Accelerated tier 1.** Upstream levelling is XP-driven, so "a level every
    session or two until 5" happens only if written down. State it as a
    milestone rule here and as a line in `## DM Style Notes`.
  - **The act-boundary exits** from `spec`. Do not put these in the arc's
    `steering_notes` — `/dm:dnd end` rewrites that field every session.
  - **The archive compression cadence.**
  - **The `audit` reminders** at roughly session 5 and 15, so they actually
    fire.
- Characters: `/dm:dnd character new`. The data root holds a global character
  roster including the finished campaign's level-20 PCs — this is a fresh world,
  so do not import them.

**Before finishing, check every file written against the load-path rule.** For
each one, name which of the three conditions it satisfies — read directly,
pointed at from the load path, or deliberately inert. A file satisfying none of
them is invisible to the DM and must be moved into a file that is read, given a
pointer, or not written at all.

Then verify by loading it — but know what a healthy load looks like, because
several prompts are normal and are **not** build failures:

- `/dm:dnd load` always asks about display mode and dice mode.
- Graph init is a hard requirement upstream, so a new campaign will run the
  init flow on first load. Expected.

What *would* mean the build is wrong: a ruleset-migration prompt (the
`**Ruleset:**` header is missing), a complaint about a malformed
`## Campaign Arc`, or a recap that cannot find the style notes or dials.

Loading also drops the session into Active DM Mode. **Stop there** — do not
begin narrating. The build is verified; play is a separate decision the player
makes.

**Done when:** the campaign loads, `dm-contract.md` resolves from the new campaign directory, every written file has been checked against the load-path rule, and nothing in `world.md` or `state.md` is still a template placeholder. Set the stage `done`.

---

## Stage: `audit`

Run at roughly session 5 and session 15 of the new campaign. This is what keeps
the contract from being a theory written in the emotional wake of an ending.

For each core contract line: cite what happened. Did it hold? Did it help?
Promote lines that worked into permanent style notes, cut lines that produced
nothing, and rewrite lines that were directionally right but badly phrased.

For each experiment: check its success condition against the record and resolve
it — adopt, revert, or extend once with a stated reason. Record the outcome
against the dispute it came from:

```bash
python ${CLAUDE_SKILL_DIR}/scripts/omega_state.py resolve <campaign> <n> "<outcome>"
```

Dispute numbers come from `dump <campaign>` with no `--stage`, which prints the
`disputed` array in order; `<n>` is the 1-based position. `status` reports
`disputes_unresolved`; the audit is not finished while that is non-zero and the
experiments have run their course.

Re-run `omega_health.py all <new-campaign>` here too — discounting the findings
that are simply "young campaign": a missing `## Continuity Archive` at session 5
is expected, since `/dm:dnd save` creates it. A missing `## DM Style Notes` is
not, and would mean `build` did not write the contract. Fifteen sessions is early
enough that a bloat pattern is cheap to correct and late enough to be visible —
if `state.md` is already growing into the load path, the archive cadence from
`tooling` is not being honoured, and that is worth catching now rather than at
session ninety.

Overcorrection is the expected failure. A contract written straight after a
campaign ends over-weights how the *ending* felt: rules like "make everything
deadly" read as wisdom on day one and as a mistake by session 12. Be willing to
cut your own lines.

**Done when:** every core line has a verdict, every experiment is resolved, `disputes_unresolved` is zero, and the audit log in `omega/contract.md` is updated. Set the stage `done`.
