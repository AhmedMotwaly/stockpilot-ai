# Risks and recovery

Related: [DECISIONS_LOG.md](DECISIONS_LOG.md), [DAILY_STUDY_PLAN.md](DAILY_STUDY_PLAN.md).

## 1. Risks

| Risk | Likelihood | Response |
|---|---|---|
| Phase 1 too dense (Python, SQL, Git, dataset) | High | Two-stage dataset; Claude Code drafts the generator, you review each part |
| Phase 2 too dense (pandas, SQL, Power BI, DAX) | High | Minimal Excel; cut dashboard pages before model documentation |
| Code runs but is not understood | Medium | Explain each function aloud; write the test before the fix |
| Windows setup problems | Medium | Day 1 steps; one terminal type (PowerShell in VS Code) |
| Invented numbers from the LLM | Medium | Python computes; claim checker; planted-error tests |
| Prompt injection through CSV text | Medium | Data treated as data; hostile fixtures |
| Secret pushed to GitHub | Low | .gitignore; check before push; revoke any exposed key at once |
| API cost | Low | Mock default; spending limit; cost logged |
| Hidden true-demand file used by the app | Low | Separate folder; test confirms the app never opens it |
| Falling behind | Medium | Cut order below |
| Job search and permit pressure | High | 45 minutes daily outside study; use evidence from Day 28 |
| Burnout | Medium | Keep rest days; cut scope before sleep |

## 2. Recovery from errors

| Situation | Steps (PowerShell, in the project folder) |
|---|---|
| A file is broken and not committed | `git restore path\to\file` returns the last committed version |
| All uncommitted changes are wrong | `git status`, then `git restore .` (loses uncommitted work) |
| A bad commit was pushed | `git revert <commit-hash>` creates a new commit that undoes it |
| Virtual environment broken | Delete `.venv`, then `python -m venv .venv`, activate, `pip install -r requirements.txt` |
| `Activate.ps1` blocked | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| `python` opens the Microsoft Store | Install Python from python.org with "Add to PATH" ticked, or use `py` |
| `ModuleNotFoundError` | Check the venv is active (prompt starts with `(.venv)`), then `pip install -r requirements.txt` |
| Tests fail after a change | Read the first failure only; fix; rerun one test with `python -m pytest tests\test_x.py -k name` |
| A secret was committed | Revoke the key at the provider first; then remove it and ask for help cleaning history |
| Database file corrupt | Delete it from `database/` and rerun the loader |

Rule: when a command fails, stop, read the full error, fix it, then continue.

## 3. Schedule slip rule

Behind by up to 2 study days: use rest days for catch-up. Behind by more than 2 study days: apply the cut order and
record the cut in DECISIONS_LOG.md.

## 4. Cut order (cut from the top; never cut tests or documentation)

1. Free online deployment of the app.
2. Branch transfer suggestions.
3. Seasonality depth beyond the basic exploration in Module D.
4. Extra charts and dashboard pages beyond the 8 required KPIs.
5. Live Claude API runs beyond one final evaluation run.
6. Warehouse productivity KPI (use a note instead).
7. Optional Holt-Winters in Project 3.

Never cut: calculation tests, data validation, evidence records, claim checker, approval workflow, audit log,
README, test and evaluation report.
