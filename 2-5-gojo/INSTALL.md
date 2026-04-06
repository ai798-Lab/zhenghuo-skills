# Installation Guide — 2.5条悟.skill

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/2-5-gojo-skill ~/.claude/skills/2-5-gojo
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/2-5-gojo-skill .claude/skills/2-5-gojo
```

## Verify Installation

In Claude Code, type:

```
会赢
```

## Update

```bash
cd ~/.claude/skills/2-5-gojo
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/2-5-gojo
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.
