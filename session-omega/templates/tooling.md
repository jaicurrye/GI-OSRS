# Tooling Audit — <campaign>

**Sessions:** <n>  **Audited:** <date>

## Health

| File | Est. tokens | Load path | Note |
|---|---|---|---|

**`state.md` breakdown** — the per-session cost:

| Section | Est. tokens | Flag |
|---|---|---|

**Missing expected sections:**

## Feature usage

| Feature | Used | Unwanted / Unknown | Note |
|---|---|---|---|
| Relationship graph | | | |
| Pinned facts | | | |
| Faction Moves | | | |
| Live State Flags | | | |
| Continuity Archive | | | |
| Dials | | | |
| Display companion | | | |
| Autorun | | | |

## Failures and friction

| What broke | When | Workaround used | Fixable? |
|---|---|---|---|

**Trust date:** *the session at which the player started keeping their own notes*

## Cross-checks against the review

*Complaints from `review` that have a configuration cause rather than a DM-behaviour
cause. These are removed from the contract and fixed here instead.*

| Review complaint | Tooling cause | Fix |
|---|---|---|

## Configuration for the new campaign

*Consumed by `build`. Every line names its finding.*

Fill what this stage can determine. The three dials are derived at `contract`
and the ruleset is confirmed at `spec` — leave them as `TBD` here rather than
guessing two stages early, and complete them before `build` reads this block.

```yaml
# decided here, from the audit
roll_mode:       # players | auto
autosave:        # on | off  (default on; only set off with a reason)
archive_cadence: # e.g. "compress every 20 sessions"
display:         # use | skip
autorun:         # use | skip

# filled at contract
difficulty:      # TBD
spotlight:       # TBD
pacing:          # TBD

# filled at spec
ruleset:         # TBD — 2014 | 2024
```

*Graph init is a hard requirement at first load upstream, so it is not a
setting — a new campaign gets the graph whether or not you ask.*

| Setting | Value | Finding |
|---|---|---|

## Extensions and custom content

**Installed now:**

| Extension | Installed | Used | Keep for campaign 2 |
|---|---|---|---|
| Autosave Stop hook | *(check with `install_autosave_hook.py --status`)* | | |
| Display companion | | | |
| Supplemental dataset | | | |

**Kept outside the system** — *what the player wrote down elsewhere, and why:*

**Placement plan** — *every item gets one of: on the load path, pointed at from
it, deliberately inert, or imported as a lazy corpus. Anything that fits none of
these is not written.*

| Item | Placement | How it gets read |
|---|---|---|
