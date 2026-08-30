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

```yaml
ruleset:        # 2014 | 2024
roll_mode:      # players | auto
autosave:       # on | off
difficulty:     # from contract
spotlight:      # from contract
pacing:         # from contract
graph_init:     # true | false — initialize at build
archive_cadence:# e.g. "compress every 20 sessions"
display:        # use | skip
autorun:        # use | skip
```

| Setting | Value | Finding |
|---|---|---|
