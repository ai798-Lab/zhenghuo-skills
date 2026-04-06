# Installation Guide — 钟离.skill

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/zhongli-skill ~/.claude/skills/zhongli
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/zhongli-skill .claude/skills/zhongli
```

## Verify Installation

In Claude Code, type:

```
钟离
```

## Update

```bash
cd ~/.claude/skills/zhongli
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/zhongli
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.
