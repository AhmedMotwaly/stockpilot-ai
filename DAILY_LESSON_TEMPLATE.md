# Daily lesson template

Every lesson uses this structure. Claude Code fills it from [DAILY_STUDY_PLAN.md](DAILY_STUDY_PLAN.md) and saves the
lesson notes as `docs/lessons/day-NN.md`. After the lesson, update [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md).

```
# Day NN, date: title

## 1. Learning objectives
- 2 to 4 measurable objectives

## 2. Previous knowledge required
- Days and files this lesson builds on

## 3. Supply chain explanation (45 min)
- Business problem first, then the concept, then a retail or warehouse example

## 4. Technical explanation (75 min)
- Concept in plain English, why it matters here, one small example

## 5. Practical demonstration
- Short worked example before the build

## 6. Step-by-step implementation (90 min)
1. Folder to open
2. Terminal to use (PowerShell in VS Code)
3. Files to create or change, with full paths

## 7. Complete code
- Full file contents, never fragments, with filename and location
- When changing a file: the complete new file and a list of what changed and why

## 8. PowerShell commands
- Each command, what it does, and the expected result

## 9. Expected output
- Exact or sample terminal output

## 10. Common errors and solutions
| Error message | Cause | Fix |

## 11. Practical exercise (30 min)
- Task first; solution only after an attempt

## 12. Knowledge check
- 3 to 5 questions; answers reviewed

## 13. Git commit instructions
- git status, git add, git commit -m "type: message", git push
- Explanation of each command

## 14. Completion checklist
- [ ] Code runs
- [ ] Tests pass
- [ ] Exercise done
- [ ] Commit pushed
- [ ] PROGRESS_TRACKER.md updated

## 15. Next lesson preview
- What comes next and what to prepare
```

## Teaching rules

1. Business problem first.
2. Supply chain concept, then technical concept.
3. Exact steps, complete files, exact PowerShell commands, expected output.
4. Explain important code sections.
5. Common errors explained.
6. Exercise before solution. Understanding checked.
7. When a command fails, stop and troubleshoot before continuing.
8. Never claim code was tested unless it ran.
9. Claude Code writes the Python. The learner directs, runs, reads, tests and explains it (D-028).
10. The learner writes short SQL queries and Excel formulas by hand, with hints first.
