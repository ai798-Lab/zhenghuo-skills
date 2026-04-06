# Installation Guide — GPT-3.5 Nostalgia.skill

## Requirements

- [Claude Code](https://claude.ai/code) CLI installed
- Git

## Install (Global — works in all projects)

```bash
git clone https://github.com/ai798-Lab/gpt-35-nostalgia-skill ~/.claude/skills/gpt-35-nostalgia
```

## Install (Per-project — run in git repo root)

```bash
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/gpt-35-nostalgia-skill .claude/skills/gpt-35-nostalgia
```

## Verify Installation

In Claude Code, type:

```
gpt35
```

## Update

```bash
cd ~/.claude/skills/gpt-35-nostalgia
git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/gpt-35-nostalgia
```

## Troubleshooting

**Skill not found?**
Claude Code looks for skills in:
1. `~/.claude/skills/` (global)
2. `.claude/skills/` in the git repo root (project-level)

Make sure you cloned into the correct location.
