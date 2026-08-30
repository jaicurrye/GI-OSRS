# Reading the tooling audit

`omega_health.py all <campaign>` produces four blocks: `files`,
`state_sections`, `features`, and `findings`. This is what they mean and what
follows from each.

## The load path is the whole game

The dnd skill is explicitly token-budgeted, and its central design decision is
that **`state.md` is read at every `/dm:dnd load` and almost nothing else is.**
NPC entries load lazily. `session-log.md` is read only on an explicit recap.
`arc.md` is read only when advancing chapters.

So:

- A 40,000-token `session-log.md` costs **nothing**. It is doing its job.
- A 12,000-token `state.md` costs 12,000 tokens **every session, forever**, and
  is the first thing to fix.

The `load_path` flag in the `files` block marks this. Do not recommend
compressing a cold file to save tokens; it saves nothing and loses history.

## Section sizes

`state_sections` breaks `state.md` down by heading, largest first, with a flag
at ~1500 estimated tokens and ~3000. Those thresholds are judgement, not limits
from the skill — treat them as "look at this", not "this is broken".

The characteristic long-campaign failure is `## Continuity Archive` growing
unboundedly. It is meant to hold condensed recaps; left uncompressed for a
hundred sessions it becomes a transcript sitting in the load path, and it will
usually be larger than every other section combined.

The fix is the skill's own compression pass, and the recommendation for the new
campaign is a **cadence** — roughly every 20 sessions — written into the new
campaign's DM Notes so it happens without the player remembering.

`missing_expected` lists sections `/dm:dnd load` looks for that aren't there.
`DM Style Notes` missing is significant: it means the per-campaign calibration
loop never ran, so nothing the table learned was carried forward automatically.

## Feature usage

Inferred from artifacts, since there is no command history to read. Each check
distinguishes a section that was *used* from one holding only its template help
text — a blank `## Pinned Facts` full of italic instructions is unused, however
many bytes it takes.

What each absence means:

| Absent | Consequence |
|---|---|
| `graph.json` | No relationship graph. On a 100-session campaign this is the main defence against continuity loss under context compaction — the thing most likely behind "the DM forgot who that was". |
| Pinned facts | The cheapest continuity tool in the skill went unused. Promises made, names that matter, running jokes — all left to ordinary memory. |
| Faction Moves | Standard 11 left no trace, so the world probably did not visibly move without the player. Cross-check against the review's "did the world feel alive?" answer. |
| Live State Flags | The compaction-survival mechanism was not maintained. Cross-check against reported continuity failures. |
| Dials unset | The DM ran on defaults for the entire campaign. Not wrong, but it means no deliberate choice was ever made about lethality, spotlight or pacing. |

An unused feature is not automatically a problem. Separate **unwanted** from
**unknown** by asking, and only the second becomes a recommendation.

## Cross-checking against the review

The tooling audit is most useful where it explains a complaint from `review`:

- "The DM kept forgetting things" + no graph, no pins, Live State Flags empty →
  the complaint is largely a configuration failure, not a model failure, and it
  is fixable in the new campaign rather than by a contract line.
- "Sessions took ages to get going" + a 12k-token `state.md` → a measured cause.
- "The world felt static" + empty Faction Moves → a mechanism that existed and
  was never used.

This matters for the contract: a problem with a configuration fix should not
also consume a core contract line. Contract lines are expensive and permanent;
a flag is free. Where the tooling audit can fix something, take it out of the
contract.

## Anything you add must be reachable

The same fact that makes the load path expensive also makes it the only thing
that exists. `/dm:dnd load` reads a fixed set of files and reaches everything
else through a pointer. There is no scan of the campaign directory, so a file
nobody points at is not "lightly used" — it is unreachable, silently, with no
error and no signal.

This is the failure mode most likely to waste real effort: a player writes a
house-rules document or a lore bible, puts it in the campaign directory
alongside the files that *are* read, and reasonably assumes the DM has it. It
never gets opened, and the absence looks exactly like the DM ignoring the rules.

Three legitimate placements, and nothing else:

| Placement | Use for |
|---|---|
| **On the load path** | Anything needed every session. Costs tokens every session, so it must be short — this is where the core contract lines go. |
| **Pointed at** | Anything needed sometimes. A line on the load path names the file and says when to read it; the situational contract tier works this way. Cheap and unbounded in size. |
| **Deliberately inert** | Records for the player, not the DM — `review.md`, `chronicle.md`. Documented as inert so nobody later assumes the DM has read them. |

Long-form material has a fourth option: `/dm:dnd import` builds a lazy corpus,
one file per chapter, indexed and never loaded at session start. It works for
any long-form text, not just published modules. A substantial written setting
should be imported, not pasted into `world.md` — pasting it puts a book on the
load path permanently.

## Extension points worth checking

- **Autosave Stop hook** (`install_autosave_hook.py`) — optional, prompts the
  continuity flush on a turn cadence. If `review` reported dropped details or
  continuity loss and this was never installed, it is a fix that costs nothing
  and spends no contract line.
- **Display companion** — installed versus actually used; TLS only matters on
  an untrusted network.
- **Supplemental dataset** (`/dm:dnd data sync`) — custom monsters, items and
  spells belong here rather than in prose, where they are searchable and do not
  sit on the load path.
- **Character portability** (`/dm:dnd character import`) — characters can move
  between campaigns, which matters if anything from the old party is wanted.

## What the player kept outside the system

The most useful question in this part: what did you write down somewhere else?

A player maintaining notes in a separate document, a spreadsheet, or their head
was compensating for something the campaign would not hold. Find out what it was
and give it a home under the placement rules above. That habit disappearing is a
larger improvement than most contract lines, because it means the system finally
holds what the player already decided was worth keeping.

## Dating the loss of trust

The one question in this stage that no script can answer: *when did you stop
trusting the DM to remember, and start keeping your own notes?*

Everything before that date is a working system. Everything after is the player
compensating. If that date is early, the tooling recommendations matter more
than anything in the contract — and the review's memory complaints should be
re-read knowing the player had already given up on it.
