# Installation Guide — 冯宝宝.skill

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/feng-baobao-skill ~/.claude/skills/feng-baobao
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/feng-baobao-skill .claude/skills/feng-baobao
```

## Verify Installation

In Claude Code, type:

```
宝儿姐
```

You should get a response in 冯宝宝's style — short, direct, Sichuan dialect.

## Update

```bash
cd ~/.claude/skills/feng-baobao
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/feng-baobao
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.

**Wrong directory?**
`~/.claude/skills/feng-baobao/SKILL.md` should exist after installation.
