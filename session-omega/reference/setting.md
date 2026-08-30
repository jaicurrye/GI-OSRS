# Taste profile, constraint sheet, and the world build

## The taste profile

Built from the review and the evidence, before any question about the new
campaign is asked. Its purpose is that the player never sees a blank field.

The profile is inferred from **engagement, not preference**. What a player says
they like and what they spent a hundred sessions doing are different data, and
the second is better. Sources, in order of trust:

1. **Recurring calibration notes** — written during play, without hindsight.
2. **Where the campaign was at its best** — the stretch, not the moment.
3. **The NPCs named without looking**, and what they had in common.
4. **What the player did when given a free hand** — which nodes they walked
   toward, which they never visited.
5. **What the interview said.** Real, but the most distorted by recency.

Contradictions between sources are findings, not noise. A player who says they
want political intrigue and whose best-remembered sessions are all dungeons is
telling you something true about both.

Write the profile as a short paragraph, not a scorecard, and show it to the
player before the constraint sheet. It is a claim about them; they should get to
argue with it first.

**Then, and only then, unseal `predict` question 5** — what the player said they
were drifting toward and sick of, recorded before the finale and before any
retrospection. The ordering is load-bearing: a profile written after reading the
stated appetite is no longer independent of it, and the comparison collapses.

Treat the two as equal witnesses. Agreement makes the constraint sheet nearly
automatic. Disagreement is presented plainly and left to the player — a player
sick of the thing the evidence says they loved is not making an error, and
neither is a player drawn to something they never once chose when it was
available. Recorded appetite and revealed engagement are different facts about
a person, and which one should govern the next hundred sessions is not an
inference this stage gets to make.

## The constraint sheet

Every field gets a **proposed value** and the **finding behind it**, one line
each. The player confirms or overrides. Present it whole, then walk the fields
they didn't immediately accept.

| Field | Notes |
|---|---|
| Premise | One sentence. What the campaign is about — meaning, not plot. |
| Tone | Where on grim↔hopeful, and how much comedy is welcome. |
| Genre texture | High fantasy, sword and sorcery, gothic, weird, planar, low-magic… |
| Scale | Personal / regional / national / cosmic — and where it *starts*. |
| Magic level | How common, how trusted, how well understood. |
| Central conflict | The thing that escalates for a hundred sessions. |
| What the campaign asks of the player | The recurring question it puts to them. |
| Hard no-gos | Content that will not appear. Ask directly; do not infer. |
| Veils | Content that exists but stays off-camera. |
| Ruleset | 2014 (SRD 5.1) or 2024 (SRD 5.2). Goes in the `state.md` header. |
| Combat share | Roughly what fraction of a session should be a fight. |
| Party size and control | Resolved in `party`, but proposed here. |

Fixed for this table, not up for re-proposal unless the player raises it: fresh
world with no continuity, designed for a long epic with act-boundary exits,
starting at level 1 with accelerated advancement through tier 1.

Ask the no-gos as a plain question even in a solo campaign. It is not a safety
ritual borrowed from a group table — it is a DM instruction, and the DM needs
it written down where it will be read at load.

## The world skeleton

Four things, and deliberately nothing else:

**Theme.** One sentence about meaning. The dnd skill's dynamic arc has a
`theme` field expecting exactly this — write it to be pasted in.

**Central conflict.** Must be *renewable*. Test it: what does this conflict look
like at session 80? If the answer is "the same, but bigger", it is a threat, not
a conflict, and it will be exhausted by session 30. Renewable conflicts have
sides that can change, costs that accumulate, and no single victory condition.

**Starting region.** Small. One town or district and what surrounds it. A
hundred-session campaign will cover a continent; it should not start on one,
because a level 1 party can't engage with a map and the player can't hold it.

**Three truths.** Three facts about the world that are load-bearing and
counter-intuitive — the things a native knows and a reader wouldn't guess. Not
lore: constraints. Each truth should rule something out.

Stop there. The rest of the world is written after `party`, shaped around the
characters that actually exist. Building the whole world first is how you get a
party of tourists in someone else's setting.

## Act-boundary exits

Designed for a long epic, but each act boundary gets a **stopping shape**: a
state the world could plausibly be left in that reads as an ending rather than
an abandonment. Note it in the arc's `steering_notes`. It costs nothing during
play and means that if life intervenes at session 40 there is an ending
available.

## Party architecture

Decide before characters, and decide it from the review's finding about why the
DM-run PCs were taken over. The options and what each actually costs:

- **One PC, DM-run companions as NPCs.** Deepest single-character interiority.
  Depends entirely on the DM playing companions as people — which is the thing
  that failed last time, so only choose it with a contract line covering it.
- **Two PCs, player-run.** A middle that most solo players land on: enough
  tactical texture for combat, few enough heads to stay inside.
- **Four PCs, player-run.** What the last campaign converged to. Full control,
  full tactical range, and the known cost is diluted interiority — the review
  should have established whether that cost was real.
- **Mixed with an explicit contract.** Player runs two, DM runs two, but with a
  contract line stating what a DM-run PC must do (have wants that conflict with
  the party's, refuse orders sometimes, act off-screen).

Then each PC needs three things: a tie to the central conflict, a tie to at
least one other PC, and something they want that the campaign can threaten. A
character missing the third is a character nothing can happen to.

Mechanical creation is `/dm:dnd character new`. This stage produces the spec.
