@AGENTS.md

# Claude Code Notes

- Claude Code loads the skills in `.claude/skills/` automatically. After editing a skill, run the validation commands in [README.md](README.md#validation-and-packaging).
- Run repository scripts with the project venv, `.venv/Scripts/python.exe` on Windows (set up as in [README.md](README.md#windows-7-zip--venv)) and `python3` elsewhere.
- Create git worktrees under a short root, a few folders below the drive rather than under a synced or deeply nested checkout, and keep `git config core.longpaths true`, because corpus paths are up to 188 characters long below the repository root and many Windows tools fail beyond 260 characters.
