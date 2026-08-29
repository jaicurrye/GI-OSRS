# Session Omega

An end-of-campaign skill for [claude-dnd-skill](https://github.com/neuralinitiative/claude-dnd-skill).

Session Zero runs before the first session. Session Omega runs after the last,
and its output *is* the next Session Zero: a reviewed campaign, a DM behaviour
contract built from what actually happened, and a new world designed around
what a hundred sessions proved you like.

## Install

```bash
cp -r session-omega ~/.claude/skills/
```

Then `/session-omega status <campaign>`, or just say "let's review the campaign".

It reads `~/.claude/dnd/campaigns/` (or `$DND_CAMPAIGN_ROOT`) and writes to
`<campaign>/omega/`. It does not modify the dnd skill, and does not touch the
old campaign's own files.

## Stages

Run in order; each is independently invocable and resumable.

| Stage | |
|---|---|
| `predict` | **Before the finale.** Seals your predictions and hopes. |
| `review` | Cold interview, no file reads, so your answers aren't anchored. |
| `evidence` | Targeted extraction, then reconciles the record against memory. |
| `chronicle` | *Optional.* Narrative keepsake, epilogues, DM reveals. |
| `contract` | Tiered DM behaviour contract plus the three table dials. |
| `spec` | Taste profile → a constraint sheet pre-filled with reasoning. |
| `world` | Setting skeleton: theme, conflict, region, three truths. |
| `party` | Party architecture, then characters tied to world and each other. |
| `build` | Writes the new campaign. `/dm:dnd load` works immediately. |
| `audit` | At session ~5 and ~15: test the contract against what happened. |

## How it works

**The interview argues back.** The DM has the record and will contradict you
from it — but only from cited record, and you always get the last word.
Deadlocks are logged as disputes and become labelled experiments with revert
conditions, not silently-adopted rules.

**Evidence is targeted, never a full sweep.** A hundred-session log doesn't fit
in a context window, so extraction pulls the parts that carry signal: the
`### DM Calibration` blocks `/dm:dnd end` has been writing after every session,
arc revisions, deaths, NPC attitude shifts, roster changes, and session cadence.
The calibration notes are the best evidence in the campaign — written during
play, without hindsight.

**The contract compiles into the dnd skill's own surfaces.** No fork. Core
lines go to `state.md → ## DM Style Notes`, which `/dm:dnd load` reads and which
overrides default DM instincts; the three dials go to `## Session Flags`. Every
core line is loaded for the life of the campaign, so the contract is a budget
rather than a wish list, and a line that merely restates one of the skill's
fourteen Standards is rejected.

**`build` never runs `/dm:dnd new`**, which would auto-generate a world and arc
over the top of the one you designed. It writes the files from the dnd skill's
templates instead.

## Layout

```
session-omega/
  SKILL.md                        stage dispatch and procedure
  reference/
    review-dimensions.md          the question bank, six dimensions
    contract.md                   the four tests, tiers, dials, experiments
    setting.md                    taste profile, constraint sheet, world build
  scripts/
    omega_paths.py                path discovery + targeted extraction
    omega_state.py                resumable progress file
  templates/
    review.md  contract.md  spec.md
```

Unofficial, unaffiliated with Wizards of the Coast or with the dnd skill's
authors.
