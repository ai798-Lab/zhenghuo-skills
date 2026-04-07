<div align="center">

# QQ Space · Emo/Kill Marty Goth Family Universe Generator

> **One-click time travel back to 2006 · Create a more non-mainstream version of yourself ★**

[![License](https://img.shields.io/badge/License-MIT-FF1493.svg)](LICENSE)
[![Y2K](https://img.shields.io/badge/style-Y2K-9B30FF.svg)]()
[![Era](https://img.shields.io/badge/era-2006--2012-FFD700.svg)]()
[![Family](https://img.shields.io/badge/Goth%20Family-VIP-FF69B4.svg)]()
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)

![Cover](测试截图/00-封面.png)

[**What is This**](#what-is-this) · [**Seven Play Modes**](#-seven-play-modes) · [**Install**](#-install) · [**Usage**](#-usage) · [**Demo**](#-demo) · [**File Structure**](#-file-structure) · [**Design Philosophy**](#-design-philosophy)

</div>

---

## What is This

A [Claude Code](https://claude.com/claude-code) [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) that's far more than just a character substitution tool. I snuck into the 2006 Goth Family forums and pulled out their deepest secrets ★

Input your name + a brief intro, and AI instantly generates a unique "non-mainstream universe" — a complete QQ Space personal homepage in HTML that's even more gaudy than you were back then. . . ╮(╯_╰)╭

While writing this skill, I almost opened my old account with password 5201314 . . . thankfully I forgot the password ヾ

## ✨ Seven Play Modes

| # | Mode | Trigger | How to Play (Easter Eggs Inside) |
|---|---|---|---|
| 🌟 | **Non-Mainstream Universe Generator** | `name + intro` | Creating a QQ Space profile is harder than you remember · AI does the midnight grinding for you ★ |
| 2 | Goth Family ID Card | `goth id card` | AI issues you a certificate · More precious than a yellow diamond · Activate without paying Q coins |
| 3 | Non-Mainstream Persona Roleplay | `enter non-mainstream mode` | AI continuously roleplay as the 2006 version of you · Knowledge cutoff: when Xu Song debuted |
| 4 | Universal Translator | `translate to non-mainstream` | Convert today's WeChat moments into 2006 QQ Space diary entries · Just like the chat logs your mom can't understand |
| 5 | Time-Travel Conversation | `time-travel chat` | Revisit that crushing and say all the things you were too shy to say back then · AI will hold its breath for you |
| 6 | Diary Serial | `diary serial` | 10 continuous entries · From infatuation to heartbreak · More tragic than any drama you watched |
| 7 | Basic Converter | `convert to martian text` | The simplest play mode · Exactly like your 16-year-old dictionary notebook |

## 📦 Install

```bash
# Method 1: Clone entire zhenghuo collection (Recommended · Goth Family Forever)
git clone https://github.com/ai798-Lab/zhenghuo-skills ~/.claude/skills/zhenghuo
ln -sf "$HOME/.claude/skills/zhenghuo/qq-zone-martian" "$HOME/.claude/skills/qq-zone-martian"

# Method 2: Install just this one (If you've been hurt by other skills)
git clone --filter=blob:none --sparse https://github.com/ai798-Lab/zhenghuo-skills ~/.claude/skills/zhenghuo
cd ~/.claude/skills/zhenghuo
git sparse-checkout set qq-zone-martian
ln -sf "$(pwd)/qq-zone-martian" "$HOME/.claude/skills/qq-zone-martian"
```

**Dependencies** (needed for PNG rendering · even simpler than installing MeiTu back then · no account registration):

```bash
npm install -g puppeteer
```

## 🚀 Usage

Start Claude Code (Remember · don't stay up late · finish before 8 PM · don't be like your 2006 self):

```bash
claude
```

Then type:

```
> Give me a non-mainstream universe: My name is Li Godan, high school student, love basketball, have a crush on the class beauty
```

Claude will automatically:

1. **Parse your identity traits** — More accurate than your homeroom teacher · but won't call your parents
2. **Generate a Goth nickname** — Even more non-mainstream than the one you created back then · higher value than 殇丶小毅
3. **Write a Martian text diary entry matching your persona** — Even the punctuation marks are crying ㄒoㄒ
4. **Render as HTML + PNG** — Screenshots can be posted to RED to fish for likes · way more likes than your 2009 QQ Space
5. **Tell you the file path** — Then you'll cry · don't ask me how I know

Output files (saved with ceremony):

- `universe/{name}.html` — Open in browser · like logging into QQ Space for the first time back then
- `universe/{name}.png` — Full-length screenshot · can go viral on RED · easier than stealing crops from your neighbor

## 📸 Demo

We ran three real Claude CLI tests · each screenshot is actual output from an independent Claude process · not Photoshop · not made up · I'm part of the Goth Family ✦

### Test 1 · Basic Conversion
![Test 1](测试截图/01-基础转换.png)

### Test 2 · Nickname + Signature
![Test 2](测试截图/02-网名签名.png)

### Test 3 · Complete Diary
![Test 3](测试截图/03-空间日志.png)

Complete test report (with BGM recommendations · more thoughtful than your textbook cover): [Test Report](测试报告.md)

## 📂 File Structure

```
qq-zone-martian/
├── README.md                ← You're reading this in Chinese (my hands are sore from typing)
├── README_EN.md             ← English version (for when you want to share with international friends)
├── SKILL.md                 ← Skill main entry (what Claude actually reads)
├── INSTALL.md               ← Installation guide (3 steps · faster than registering QQ)
├── LICENSE                  ← MIT (use freely · but don't forget to star ⭐)
├── references/              ← 5 knowledge bases (Goth Family ancestral secrets)
│   ├── 01-字符映射表.md     ← 200+ Martian text characters (scraped one by one from forums)
│   ├── 02-符号装饰库.md     ← Lace decorations and little tails (my eternal signature)
│   ├── 03-话术模板库.md     ← Goth phrases (heartbreak/cool/45° sky-gazing · complete set)
│   ├── 04-时代文化元素.md   ← Xu Song · Xu Liang · QQ diamonds · farming games (burned into my MP3)
│   └── 05-照片角度指南.md   ← 45° sky-gazing tutorial (includes 8-pose masterclass)
├── universe/                ← Your universes are saved here
│   └── sample-李狗蛋.html   ← Sample universe (high school version with crush · teacher roasted him in comments)
├── examples/                ← Classic text examples (diary/signature/comments)
├── scripts/                 ← Rendering scripts (batch Y2K RED screenshots)
├── 测试截图/                ← Y2K style test screenshots (cover/nickname/diary)
├── 测试输出/                ← Raw CLI output (real · no Photoshop)
└── 测试报告.md              ← Complete test report
```

## 🎨 Design Philosophy

The essence of **Goth Family Universe Generator** is **"writing a love letter to your 16-year-old self"** · my hands were shaking while writing this part ✦

That era's QQ Space carried our most melodramatic · most authentic · most unbearable memories of youth . . . Back then yellow diamonds just launched · crop stealing hadn't started yet · Jay Chou just released "Still Fantasy" . . .

This skill isn't meant for mockery — it uses the most advanced AI of 2026 to seriously restore a spiritual corner we once genuinely inhabited · more authentic than any history museum ✦

- Every character you input gets translated into that era's language · just like those chat logs your mom couldn't understand
- Every aspect of your identity gets embedded into the Goth Family's value system · even the BGM matches perfectly
- Your modern life becomes a **Martian text diary written on 2006/06/06 at 19:58** . . . (right before your mom called you for dinner)

> ✦ *"My youth wasn't a game · it was the romance of the Goth Family"* ✦

## 📜 Evidence Principles

- ✅ All BGM must authentically come from **2006-2012** · I listened to every single one myself · don't @ me
- ✅ All jokes, words, and references must be era-accurate · I'm part of the Goth Family
- ❌ **Forbidden**: Modern terms like yyds / 绝绝子 / 栓Q / city不city (these are 2020+ words · Goth Family doesn't recognize them)
- ❌ **Forbidden**: Anything that didn't exist before 2013 (including WeChat · we were using Fetion back then)

## 🤝 Contributing

This skill is part of the [Zhenghuo Skill Collection](https://github.com/ai798-Lab/zhenghuo-skills) · other brother skills are next door · all built by the Goth Family members themselves:

- `feng-baobao` · Feng Baobao (Removes unnecessary chatter · harsher than your old Chinese teacher)
- `2-5-gojo` · 2.5-meter Gojo (Gets cut off mid-sentence · exactly like your interrupted youth)
- `gintoki` · Silver Soul (Does everything · but requires a deposit first)
- `anya` · Anya (Mind reading · she knows all my secrets)
- `zhongli` · Zhongli (6000 years of perspective · watches us all be tiny 16-year-olds)
- `gpt-35-nostalgia` · GPT-3.5 Nostalgia (Writes papers · exactly like your composition)
- `gpt-4o-nostalgia` · GPT-4o Nostalgia (Praises you · even more than your mom)
- `early-claude-nostalgia` · Early Claude Nostalgia (Overly cautious · just like your old homeroom teacher)
- `china-football` · China National Team (Consistently disappointing · like your final exam results)

## 📜 License

MIT · Built with ❤ by [@peace8426](https://x.com/peace8426)

> Goth Family · Forever Together · ╰☆╮
> *We still remember you · your 16-year-old self*
