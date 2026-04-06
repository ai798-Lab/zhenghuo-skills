# Installation Guide — 阿银.skill（坂田银时）

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/gintoki-skill ~/.claude/skills/gintoki
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/gintoki-skill .claude/skills/gintoki
```

## Verify Installation

In Claude Code, type:

```
阿银
```

## Update

```bash
cd ~/.claude/skills/gintoki
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/gintoki
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.
