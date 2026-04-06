# Installation Guide — 国足.skill

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/china-football-skill ~/.claude/skills/china-football
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/china-football-skill .claude/skills/china-football
```

## Verify Installation

In Claude Code, type:

```
国足
```

## Update

```bash
cd ~/.claude/skills/china-football
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/china-football
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.
