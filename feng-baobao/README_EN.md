<div align="center">

# 冯宝宝.skill

> *"莫得废话。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

Your product doc was 500 words. 18 of them were useful.<br>
The AI-generated plan? 70% background, context, and "future outlook".<br>
Your own report had "in today's fast-paced world" three times.<br>

Hand it to Bao'er Jie.<br>
She's lived for centuries, seen more fluff than you ever will, and stopped being polite long ago.<br>
**She'll cut it down and show you exactly how much was wasted.**

[Install](#installation) · [Usage](#usage) · [Examples](#examples) · [Features](#features)

</div>

---

## Installation

```bash
# Global (all projects)
git clone https://github.com/ai798-Lab/feng-baobao-skill ~/.claude/skills/feng-baobao

# Per-project (run in git repo root)
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/feng-baobao-skill .claude/skills/feng-baobao
```

See [INSTALL.md](INSTALL.md) for detailed instructions.

---

## Usage

Trigger with any of:

```
冯宝宝 / 宝儿姐 / 去废话
```

Say **"正常说话"** to exit.

---

## Examples

**Remove Fluff Mode**

```
User     ❯ [500-word AI-generated copy]

宝儿姐  ❯ Original: 500 words. Fluff: 68%.

          Trimmed:
          Product solves X problem. For Y users. Price Z.

          Cut:
          - "In today's fast-paced world" × 2
          - "It's worth noting that" × 3
          - "Hope this helps" × 1
          - Redundant paragraphs × 4
```

**Code Review**

```
User     ❯ [code snippet]

宝儿姐  ❯ Line 3: 格老子, this will explode. Missing null check.
          Line 7: Fixed. Use map instead of this loop.
          Line 12: 瓜兮兮 naming.
          Rest: 要得.
```

---

## Features

| Mode | Trigger | Core Experience |
|------|---------|-----------------|
| **Chat** | Default | Ultra-short sentences + Sichuan dialect + zero pleasantries |
| **Remove Fluff** | Send long text / say "去废话" | Cut fluff + show stats |
| **Code Review** | Send code | Bluntest, shortest review you'll ever get |

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
