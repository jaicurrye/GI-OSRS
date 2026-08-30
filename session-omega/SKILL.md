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

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py roots
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py campaigns
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_state.py status <campaign>
```

`roots` reports the data root, and whether the dnd skill's `templates/` were
found — `build` needs them. If `dnd_skill_root` is null, ask the player where
the dnd skill is installed rather than guessing or writing files from memory.

If no progress file exists: `omega_state.py init <campaign> [--new-campaign N]`.

**Record every answer as it is given**, not at the end of a stage:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_state.py record <campaign> <stage> <key> --stdin <<'ANS'
<the player's answer, verbatim>
ANS
```

Verbatim. Do not summarise the player into their own review — a paraphrase made
at the moment of writing is a paraphrase you will later treat as evidence.

Outputs land in `<campaigns>/<campaign>/omega/`: `progress.json`, `review.md`,
`contract.md`, `spec.md`, `chronicle.md`.

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

Questions 1–4 unseal at `evidence`. **Question 5 unseals at `spec`**, not
earlier — it is a snapshot of unprompted creative appetite taken before a
hundred sessions of retrospection reframe it, and reading it during the review
would let it steer the very findings it is supposed to be tested against.

Then stop. Do not offer opinions on the predictions, do not foreshadow, and do
not let the answers influence how the finale is run. This last rule is a
constraint on the DM more than the player: having just read what the player
hopes for and fears, running the finale straight becomes hard, and delivering
the hoped-for thing would write the answer key and then grade against it.

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
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_state.py dispute <campaign> "<the claim>" \
  --dm "<what the record shows>" --player "<what they hold>"
```

Disputed items are not failures of the interview. They are the most interesting
thing it produces, and `contract` turns them into labelled experiments.

Watch for the failure this posture creates: a player who starts softening real
complaints to avoid the argument. If answers get shorter and more agreeable
after a disagreement, name it, drop the pushback for a few questions, and come
back to the softened answer later.

Write `omega/review.md` as you go.

---

## Stage: `evidence`

Now read. Targeted only — never sweep a 100-session log.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py extract <campaign> \
  --what calibration,arc,mortality,npcs,party,sessions
```

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
- `party` — the roster changes. For this table specifically, find the session
  where DM-run PCs became player-run, and reconstruct why.
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

---

## Stage: `tooling`

A different axis from everything else in Session Omega. `review` and `contract`
ask whether the DM played well; this asks whether the *machinery* served the
table. After a hundred sessions a campaign accumulates real operational debt,
and almost all of it is invisible during play — it shows up as sessions that
start slowly, continuity that quietly degrades, and features that were there the
whole time and never got used.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_health.py all <campaign>
```

Read `reference/tooling.md` for what each number means and the fixes that
follow from it. Output: `omega/tooling.md`. Its config section feeds `build`.

The audit has four parts. Run all four; they inform each other.

### 1. Health and efficiency — the numbers

The single distinction that matters: **`state.md` is read at every
`/dm:dnd load`; everything else is read on demand.** A large `session-log.md`
costs nothing. A large `state.md` is a tax paid at the start of every session
for the life of the campaign, and it is the most common thing wrong with a long
campaign.

`omega_health.py all` reports per-section token estimates inside `state.md` and
flags the known patterns. The usual culprit is `## Continuity Archive` growing
without ever being compressed, which turns the load path into a transcript.

### 2. Feature usage — what the campaign paid for and never used

The script infers usage from artifacts: whether the relationship graph was ever
initialized, whether pinned facts exist, whether Faction Moves was ever written
to, which dials were set, whether Live State Flags was maintained.

Two different findings live here, and they need separating:

- **Unused because unwanted** — fine. Note it and move on.
- **Unused because unknown** — the player didn't know the feature existed, or
  forgot it after session three. This is the valuable category, and the fix is
  usually a line in the new campaign's setup rather than a habit the player has
  to remember.

Ask the player directly about anything that came back unused: did you know about
this, and would you have wanted it?

### 3. Failures and friction — what actually broke

Interview, not measurement. The record rarely contains its own failures.

- When did you have to correct the DM about something that had happened?
- Did you ever hand-edit a campaign file? What were you fixing?
- Did anything crash, hang, or need restarting? The display companion, autorun?
- Which commands did you try once and abandon? What went wrong?
- Was there a point where you stopped trusting the DM to remember, and started
  keeping your own notes? When?

That last one is the most important question in this stage. It dates the moment
the tooling stopped being trusted, and everything before that date is a working
system while everything after is a workaround.

### 4. Configuration for the new campaign

Turn the findings into settings, written as a block that `build` consumes
directly. Every recommendation names the finding behind it.

- **Ruleset** — 2014 or 2024, set in the `state.md` header so first load doesn't
  prompt for a migration.
- **Dials** — `difficulty`, `spotlight`, `pacing`. These come from `contract`,
  but flag any that went unset for the whole last campaign: running on defaults
  for a hundred sessions is a finding, not a neutral choice.
- **`roll_mode`** — `players` or `auto`, from what the last campaign actually
  felt like rather than what was chosen at the start.
- **`autosave`** — on unless there is a specific reason. Off is how continuity
  gets lost to compaction.
- **Graph from session one.** If the last campaign never initialized the
  relationship graph, initialize the new one at `build`. It is the main defence
  against continuity loss on exactly the kind of campaign this table runs.
- **Archive discipline.** If `## Continuity Archive` bloated the load path, set
  a compression cadence now — a pass every ~20 sessions — and write it into the
  new campaign's DM Notes so it actually happens.
- **Display and autorun** — recommend from real usage, not from what sounds
  appealing. A companion that was started twice in a hundred sessions is not
  part of this table's setup.

### 5. Extensions and custom content

What is installed, what is worth installing, and what custom material the new
campaign should carry.

**The load-path rule, before anything else.** The dnd skill reads a fixed set of
files — `state.md`, `world.md`, `npcs.md`, `session-log.md`, `arc.md`,
`characters/` — and reads anything else only when something on the load path
points at it. A markdown file dropped into the campaign directory is therefore
*never read*, and gives no signal that it isn't being used. A `house-rules.md`
sitting next to `state.md` can be invisible for a hundred sessions.

So every file this process creates must satisfy one of three conditions, and
`build` enforces it:

1. It is one of the files `/dm:dnd load` already reads, or
2. Something on the load path points at it, the way the situational contract
   tier is reached through a pointer line in `## DM Style Notes`, or
3. It is deliberately inert — a record for the player, like `omega/review.md`,
   and is documented as such.

A file that satisfies none of these should not be written. If custom content
cannot be given a pointer, it belongs inside a file that is already read.

**Check what is installed.**

- **The autosave Stop hook** (`install_autosave_hook.py`) — optional, and
  prompts the continuity flush on a turn cadence as a backstop to the
  scene-boundary habit. Ask whether it was installed. If continuity loss or
  dropped details came up in `review` and the hook was never installed, that is
  a concrete fix and it costs no contract line.
- **The display companion** — installed, and actually used? Its TLS setup only
  matters on an untrusted network.
- **Supplemental data** (`/dm:dnd data sync`, the `data/` dataset) — whether
  custom monsters, items or spells were ever added, and whether the ruleset
  dataset is current.

**Custom content worth carrying forward.** Ask what the player wrote, wanted to
write, or kept outside the system entirely — house rules, a lore document,
custom monsters, a list of names, notes they maintained by hand. Anything kept
in a separate document *because the campaign wouldn't hold it* is the important
answer here: it means the player was compensating for a gap, and the compaction
of that habit into the new campaign is a real improvement.

For each item, decide where it lives under the load-path rule above. Most house
rules belong in the situational contract file, reached by the pointer that is
already there. Custom monsters and items belong in the supplemental dataset, not
in prose. A lore bible belongs in `world.md`, or as a corpus if it is long.

**Long-form material.** `/dm:dnd import` builds a lazy corpus — one file per
chapter under `source/`, indexed, and never loaded at session start. That
machinery works for any long-form text, not only published modules. If the
player has a substantial written setting they want the DM to know, importing it
is the right shape; pasting it into `world.md` puts it on the load path
permanently and is not.

Record the outcome as an extensions block alongside the config block, naming for
each item what it is, where it will live, and how it gets read.

---

## Stage: `chronicle` *(optional)*

Skip on request; it costs a generation pass and produces nothing the next
campaign needs. It is for the player, not the process.

A narrative retelling — acts and turning points, the NPCs who mattered and what
became of them, the party's climb from 1 to 20, an epilogue for each character,
and the DM's reveals: the plots they never uncovered, the NPC whose motive was
never explained, what would have happened down the road not taken.

Write it as story, not analysis. Read from `## Continuity Archive` and
`session-log.md` for material. Output: `omega/chronicle.md`.

---

## Stage: `contract`

See `reference/contract.md` for the full procedure, the dial mapping, and the
test every candidate line must pass.

In short: a **tiered** DM behaviour contract, sized by what the review actually
found rather than a fixed count.

- **Core** → `state.md → ## DM Style Notes` in the new campaign. Read at every
  `/dm:dnd load`, overrides default DM instincts. Every line here costs context
  for the life of the campaign, so it must earn its place.
- **Situational** → `omega/contract.md`, consulted when a matching situation
  arises rather than loaded every session.
- **Dials** → `state.md → ## Session Flags`: `difficulty`, `spotlight`,
  `pacing`. Set explicitly, with the review finding that justifies each.
- **Experiments** → disputed items, written with a success condition and a
  revert condition, resolved at `audit`.

---

## Stage: `spec`

See `reference/setting.md`.

Derive a taste profile from the review and the evidence — what the player
*engaged with*, which is not what they would say if asked cold. Then pre-fill
the constraint sheet, showing the proposed value and the finding behind it for
every field. The player confirms or overrides each one.

Never present a blank questionnaire. The work of this stage is doing the
inference so the player only has to react to it.

**Unseal question 5 from `predict` here**, and only after the taste profile is
written — the profile must be derived from evidence before the player's stated
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

---

## Stage: `build`

Write the new campaign's files directly from the dnd skill's own templates.

**Do not run `/dm:dnd new`.** It auto-generates a world seed, factions and a
three-act arc, which would overwrite or fight everything `world` and `party`
produced.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/omega_paths.py roots   # for templates_dir
```

Copy `state.md`, `world.md`, `npcs.md`, `session-log.md` from `templates/` into
`<campaigns>/<new-campaign>/`, then populate:

- `state.md` header: name, date, session count 0, and the **ruleset** line
  (`**Ruleset:** 2014` or `2024`) — a campaign without it triggers a migration
  prompt on first load.
- `## DM Style Notes` — the core contract. **Add this section**; the blank
  template does not include it, but `/dm:dnd load` reads it.
- `## Session Flags` — the three dials, plus `roll_mode` and `autosave` from
  the `tooling` config block.
- `## Campaign Arc` — the dynamic-arc YAML block, filled from `world`.
- `world.md → ## Adventure Nodes` — the opening 3–5 nodes as situations.
- `characters/` — via `/dm:dnd character new`.
- Anything else the `tooling` config block calls for: initialize the
  relationship graph if the last campaign never had one, and write the archive
  compression cadence into `## DM Notes` so it happens without being
  remembered.
- The `tooling` extensions block: install what it calls for, and place each
  piece of custom content where that block assigned it.

**Before finishing, check every file written against the load-path rule.** For
each one, name which of the three conditions it satisfies — read directly,
pointed at from the load path, or deliberately inert. A file satisfying none of
them is invisible to the DM and must be moved into a file that is read, given a
pointer, or not written at all.

Then verify: run `/dm:dnd load <new-campaign>` and confirm it reads the arc,
the dials and the style notes without prompting for a migration or repair.
A campaign that needs hand-fixing on first load was not built.

---

## Stage: `audit`

Run at roughly session 5 and session 15 of the new campaign. This is what keeps
the contract from being a theory written in the emotional wake of an ending.

For each core contract line: cite what happened. Did it hold? Did it help?
Promote lines that worked into permanent style notes, cut lines that produced
nothing, and rewrite lines that were directionally right but badly phrased.

For each experiment: check its success condition against the record and resolve
it — adopt, revert, or extend once with a stated reason.

Re-run `omega_health.py all <new-campaign>` here too. Fifteen sessions is early
enough that a bloat pattern is cheap to correct and late enough to be visible —
if `state.md` is already growing into the load path, the archive cadence from
`tooling` is not being honoured, and that is worth catching now rather than at
session ninety.

Overcorrection is the expected failure. A contract written straight after a
campaign ends over-weights how the *ending* felt: rules like "make everything
deadly" read as wisdom on day one and as a mistake by session 12. Be willing to
cut your own lines.
