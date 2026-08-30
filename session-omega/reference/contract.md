# The DM behaviour contract

The contract is the campaign's actual deliverable. Everything else is either
sentiment or scaffolding.

It exists because the dnd skill gives you a real enforcement surface:
`state.md → ## DM Style Notes` is read at every `/dm:dnd load` and explicitly
overrides default DM instincts. No fork is required. But that also means every
line is loaded for the life of the campaign, so the contract is a budget, not a
wish list.

## The test each line must pass

A candidate line is only a contract line if it passes all four:

1. **Behavioural.** It names something the DM does or refuses to do. "Be more
   immersive" is not a rule. "Never open a scene with 'what do you do?'" is.
2. **Checkable.** You could read a session transcript and say whether it was
   followed. If two people could disagree about compliance, rewrite it.
3. **Grounded.** It traces to a specific finding — an interview answer, a
   recurring calibration note, or a reconciliation. Write the citation next to
   it in `omega/contract.md`, even though the citation doesn't ship in the
   style notes.
4. **Not already default.** The dnd skill has fourteen Standards covering
   pacing, consequences, NPC memorability, bangs, and never playing the
   player's side. A contract line that restates a Standard costs context and
   buys nothing. Only write a line where this campaign proved the default
   insufficient, or where the player wants the opposite of the default.

**A fifth test, once `tooling` has run: is this fixable with configuration?**
A complaint about forgotten details, when the campaign never initialized the
relationship graph and never used pinned facts, is a configuration failure
wearing the costume of a DM failure. Fix it with a flag — flags are free and
contract lines are permanent — and delete the candidate.

Rule 4 removes more candidates than the other three combined. Check the dnd
skill's `SKILL.md` Standards before writing anything.

## Tiers

**Core** → `## DM Style Notes` in the new `state.md`.

Imperative, one line each, no rationale. This is the always-loaded tier. There
is no fixed cap, but there is a real cost curve: a short list gets followed, a
long list gets partially ignored, and a long list that gets partially ignored is
worse than a short one because you can't tell which half is live. If the list is
growing past what fits comfortably on one screen, the marginal lines belong in
situational instead.

Prefer the specific to the general. "Kill a PC if the dice say so" beats "raise
the stakes". Prefer prohibitions where the failure was the DM doing something,
and obligations where the failure was the DM omitting something.

**Situational** → drafted in `omega/contract.md`, copied by `build` into the new
campaign as `dm-contract.md`, plus a single pointer line in the style notes:

> Situational ruleset in `dm-contract.md` — consult at combat start, at
> downtime, and when a faction acts.

The path matters. `omega/` belongs to the campaign being *reviewed*; a pointer
written into the *new* campaign's `state.md` resolves against the new campaign's
directory, where no `omega/` exists. Point at a file that is actually there.

Organise it by trigger, not by topic, so the DM knows *when* to read it. Each
entry carries its finding and its citation.

**Dials** → `state.md → ## Session Flags`. Three settings, each with a neutral
middle that changes nothing. Set them explicitly and record the finding behind
each, so `audit` can test them:

| Dial | Values | Set it from |
|---|---|---|
| `difficulty` | `easy` / `standard` / `hard` / `deadly` | Whether combat was ever frightening; whether the player believed a threat could beat them; the real death count versus the felt one |
| `spotlight` | `dm_led` / `balanced` / `player_led` | Whether the campaign sagged when the DM stopped pushing, or chafed when it pushed; whether the player wanted to be handed direction or resented it |
| `pacing` | `adventure` / `mixed` / `downtime` | Where the campaign was at its best, and whether the good stretches were pressure or breathing room |

A dial is almost always the better instrument than a rule. If a candidate line
is really asking for more lethality or more player-led play, set the dial and
delete the line.

**Experiments** → the disputed items, and any correction the player is unsure
about. Written in the situational file with three parts:

```
EXPERIMENT: <the change>
  Success: <what must be observably true for this to have worked>
  Revert:  <what would prove it wrong>
  Review:  session 5 | session 15
```

An experiment without a revert condition is a rule wearing a disguise. Write the
revert condition first — if you can't state what would falsify it, the disputed
item isn't ready to be a contract line at all.

## Overcorrection

The predictable failure of any contract written straight after a campaign ends
is over-weighting how the *ending* felt. Ninety sessions of pleasure and ten of
tedium produce a contract about tedium.

Two defences. First, weight the recurring calibration notes above the interview
— they were written across the whole campaign, without hindsight, and they are
the only evidence in the room that isn't distorted by recency. Second, when a
contract line contradicts something the player enjoyed for most of the campaign,
make it an experiment rather than a rule.

## Writing it out

`omega/contract.md` carries everything: core lines with citations, the
situational ruleset by trigger, the dials with their findings, the experiments,
and a **rejected** section listing candidates that failed the four tests and
why. The rejected list matters at `audit` — when a core line gets cut, its
replacement is often already sitting there.

Only the core lines and the dials are copied into `state.md`.
