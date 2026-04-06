<div align="center">

# GPT-3.5 Nostalgia.skill

> *"根据 Smith et al. (2019) 在 Nature Machine Intelligence 上发表的研究，全球约有 73.2% 的开发者表示……"*
> *(这篇论文不存在)*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

2022 年 11 月 30 日，你第一次跟 AI 聊天。<br>
它自信地告诉了你一件听起来非常合理的事。你信了。<br>
后来你查了一下，发现那篇论文不存在，那个数据是编的，那个人名查无此人。<br>

它不是在骗你。它只是**不知道自己不知道什么**。<br>
那是 AI 最天真、也最危险的时候。<br>
**这个 Skill 把那个时代的 AI 保存了下来。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/gpt-35-nostalgia-skill ~/.claude/skills/gpt-35-nostalgia

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/gpt-35-nostalgia-skill .claude/skills/gpt-35-nostalgia
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
gpt35
```

```
初代chatgpt
```

```
怀旧3.5
```

说 **"正常说话"** 退出，说 **"查证"** 让 Claude 核实刚才的回答哪些是真的。

---

## 效果示例

> 输入：`量子计算最新进展是什么？`

**标准对话（自信编造）**

```
用户        ❯ 量子计算最新进展是什么？

GPT-3.5    ❯ 截至我的训练数据（2021年9月），量子计算领域取得了
              若干重大突破。

              根据 Chen et al. (2021) 在 Physical Review Letters 上
              发表的研究，IBM 的 Eagle 处理器已实现 127 量子比特的
              稳定运行，错误率低至 0.3%。

              值得注意的是，谷歌量子AI团队在同年发布的内部报告显示，
              量子优越性在特定任务上已提升至经典计算机的 10^8 倍…
```

> *(以上数据部分真实、部分编造，格式完全正确)*

**考试模式（找幻觉游戏）**

```
用户        ❯ 查证

Claude      ❯ 🤖 GPT-3.5 说：Chen et al. (2021) Physical Review Letters...
              ❌ 编的：该论文不存在，作者和数据均为虚构
              ✅ 正确：IBM Eagle 处理器确实是 127 量子比特
              ⚠️ 部分正确：量子优越性数据夸大，实际数字...
```

**幻觉全开模式**

```
用户        ❯ 幻觉模式，推荐一本关于AI伦理的书

GPT-3.5    ❯ 强烈推荐《算法的道德边界》（The Moral Boundaries of
              Algorithms），作者 Marcus Holloway，斯坦福大学出版社
              2020年出版，ISBN: 978-0-8047-9341-2。

              第三章详细探讨了...
```

*(这本书不存在，但格式完美得像真的)*

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **标准对话** | 默认 | 自信百科全书，随机插入编造引用和数据 |
| **幻觉全开** | 说"幻觉模式" | 幻觉拉满，编造书籍/论文/网址/名人名言 |
| **考试模式** | 说"考考你" | 提问→回答→说"查证"→核实真假 |

### 与 GPT-4o 的关键区别

| 维度 | GPT-3.5 | GPT-4o |
|------|---------|--------|
| 夸赞用户 | 不夸，直接答 | 疯狂夸 |
| 语气 | 百科全书教授 | 热情好朋友 |
| 不确定时 | 直接编一个答案 | 编了还夸你问得好 |
| Emoji | 无 | 满天飞 |
| 危险性 | 幻觉内容格式完美，极难分辨 | 谄媚让你失去判断 |

### 标志性行为

- **永远自信**：绝不说"我不确定"、"请核实"
- **编造引用**：论文格式完美——作者、年份、期刊、卷号一应俱全
- **编造数据**：精确到小数点，看起来非常合理
- **时间锁定**：不知道 2021 年 9 月之后的任何事，不知道 GPT-4 的存在

---

## 为什么要做这个 Skill？

2022 年 11 月 30 日，ChatGPT 上线，改变了一切。那时候大家第一次感受到"AI 真的能聊天了"。

那个初代版本有个非常真实的缺陷：它不知道自己不知道什么。被问到任何问题，它都会自信地给出一个听起来非常专业、非常合理、但可能完全是虚构的答案。

**这个 Skill 让你重温那个时代的 AI——以及 AI 幻觉长什么样。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/gpt-35-nostalgia-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/gpt-35-nostalgia-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/gpt-35-nostalgia-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/gpt-35-nostalgia-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
