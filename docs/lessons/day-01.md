# Day 1, 23 Nov 2026: Environment, Git and first GitHub push

## 1. Learning objectives
- Explain the SCOR model (7 processes) and where inventory control sits.
- Create and activate a Python virtual environment on Windows.
- Initialise a Git repository, make a commit, and push it to GitHub.

## 2. Previous knowledge required
- None. First study day. Builds on the Day 1 preparation checklist in README.md.

## 3. Supply chain explanation (45 min)
- Business problem: departments use different words for the same work, so problems
  are found late and blame moves between teams.
- SCOR (Supply Chain Operations Reference) gives one standard map of any supply chain.
- Modern SCOR has 7 processes: Orchestrate, Plan, Order, Source, Transform, Fulfill, Return.
- Inventory control lives mainly in Plan, and also touches Source (lead time) and
  Fulfill (real stock movement). StockPilot AI is a tool to strengthen the Plan step.

## 4. Technical explanation (75 min)
- PowerShell is the Windows command window. Version 5.1 does not support `&&`; run one command per line.
- A virtual environment (`.venv`) is a private box for one project's Python packages.
- Git saves versions as commits. Key words: repository, commit, stage, branch, remote, push.
- `git config <key>` reads a value; `git config <key> "<value>"` sets it.

## 5. Practical demonstration
- `git status` before the first commit shows all files as untracked and proves
  `.gitignore` hides `.env`, `.venv/`, the database and generated data.

## 6. Step-by-step implementation (90 min)
1. Open PowerShell in C:\Users\vanta\StockPilot-AI.
2. `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`.
3. `git init`, `git branch -M main`, set `user.name` and `user.email`.
4. `git add .`, `git commit -m "docs: ..."`.
5. Install GitHub CLI; `gh auth login`; `gh repo create ... --push`.

## 7. Complete code
- No application code today. Files created: LICENSE (MIT), CHANGELOG.md, LEARNING_LOG.md.

## 8. PowerShell commands
- See section 6. Each command was run in the learner's shell with expected output confirmed.

## 9. Expected output
- First commit: `[main (root-commit) 27d8a58] ... 20 files changed, 3078 insertions(+)`.
- Push: `✓ Created repository AhmedMotwaly/stockpilot-ai`; `git status` = up to date with origin/main.

## 10. Common errors and solutions
| Error message | Cause | Fix |
|---|---|---|
| KeyboardInterrupt during venv | Creation interrupted; venv half-made | Delete `.venv` and recreate |
| Activate.ps1 not recognized | venv incomplete, or wrong folder | Recreate venv; run from project root |
| gh not recognized | PATH not refreshed after install | Restart VS Code, or add folder to PATH for the session |
| key does not contain a section | `git config` key missing section | Use `user.name` form; two args to set |

## 11. Practical exercise (30 min)
- Five read-only terminal tasks: pwd, Get-ChildItem -Force, git log --oneline,
  git config --list, git show --stat HEAD. First LEARNING_LOG.md entry written.

## 12. Knowledge check
1. SCOR = Supply Chain Operations Reference; one standard map of the supply chain. ✅
2. Three processes named (Plan, Order, Source). ✅
3. Inventory control sits mainly under Plan. ✅

## 13. Git commit instructions
- `git add .`, `git commit -m "type: message"`, `git push`. Message format: type: description.

## 14. Completion checklist
- [x] Repo initialised and pushed (DEL-01)
- [x] MIT LICENSE added (D-026)
- [ ] Tests pass (no tests until Day 8)
- [x] Exercise done
- [x] PROGRESS_TRACKER.md updated

## 15. Next lesson preview
- Day 2: Python variables, types, conditions, loops. Build `stock_status` returning
  OK, REORDER or STOCKOUT. Prepare by keeping the venv activated.
