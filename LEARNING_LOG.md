# Learning log

A short, honest note after each study day. What I did, what I learned, what confused me.
Newest entry on top.

## Day 1 — 23 Nov 2026

**Topics:** SCOR model (7 processes), where inventory control sits, PowerShell basics,
Python virtual environment, first Git commands, GitHub.

**What I did:**
- Learned the SCOR model and that inventory control lives mainly in the Plan process.
- Created and activated a Python virtual environment (`.venv`).
- Turned the project folder into a Git repository (`git init`).
- Made my first commit and pushed the project to GitHub.
- Installed GitHub CLI (`gh`) and logged in.
- Repository is live: https://github.com/AhmedMotwaly/stockpilot-ai

**What I learned:**
- `git config <key>` reads a value; `git config <key> "<value>"` sets it.
- `.gitignore` keeps `.env`, `.venv/`, the database and generated data out of GitHub.
- The difference between `.git` (the repository engine) and `.venv` (the local Python box).
- `core.autocrlf=true` handles Windows line endings.

**Problems and fixes:**
- The first `venv` creation was interrupted and left half-made. Fix: delete `.venv` and recreate it.
- `gh` was not recognised after install. Fix: it needs a full VS Code restart (or add its folder to PATH for the session).
- A stray file `how --stat HEAD` was created by a mistyped command and removed before committing.

**Questions for next time:**
- (write any question here)

**Confidence today (1-5):** 
- 2 (As I feel I learned nothing in Supply Chain yet, most of the lessons focused in Github!!)