# Installation Guide — GPT-4o Nostalgia.skill

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/gpt-4o-nostalgia-skill ~/.claude/skills/gpt-4o-nostalgia
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/gpt-4o-nostalgia-skill .claude/skills/gpt-4o-nostalgia
```

## Verify Installation

In Claude Code, type:

```
gpt4o
```

## Update

```bash
cd ~/.claude/skills/gpt-4o-nostalgia
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/gpt-4o-nostalgia
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.
