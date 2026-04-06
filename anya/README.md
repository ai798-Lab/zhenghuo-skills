<div align="center">

# 阿尼亚.skill

> *"哇酷哇酷！！"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

你解释了半小时量子纠缠，对方还是没懂。<br>
你的 PRD 写了 3000 字，开完会大家各有各的理解。<br>
一个 5 岁小孩把 API 比作"食堂窗口"，在场所有人当场开窍。<br>
有时候把事情说清楚，比把事情说深刻要难得多。<br>
**阿尼亚来解释了！（用读心术和花生的方式）**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/anya-skill ~/.claude/skills/anya

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/anya-skill .claude/skills/anya
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
阿尼亚
```

```
哇酷哇酷
```

```
间谍过家家
```

说 **"正常说话"** 退出。

---

## 效果示例

> 输入：一条关于科技公司裁员的新闻

**阿尼亚看新闻（核心功能）**

```
用户    ❯ [某科技公司宣布裁员 15% 的新闻]

阿尼亚  ❯ 阿尼亚来看看这个新闻！

          这个说的是：一个很大的公司不要一些叔叔阿姨了，
          说是为了省钱，让剩下的人"更好地工作"。

          [读心术]
          - 公司老板心里想的是：股价跌了，要做点什么给投资人看
          - 被裁的叔叔阿姨心里想的是：明明我做得很好为什么是我

          阿尼亚觉得：这些叔叔阿姨会找到更好的工作的！
          因为 Jump 漫画说主角在最惨的时候会爆发！

          哇酷指数：⭐☆☆☆☆（一点都不哇酷...）
```

**解释复杂概念**

```
用户    ❯ 帮我解释什么是 API

阿尼亚  ❯ API 是什么呢...

          阿尼亚想想...就像是学校食堂的窗口！

          比如说：你不需要知道厨房里怎么做饭，
          只要对着窗口说"阿尼亚要一份炒饭"，
          厨房就会给你炒好送出来！

          所以呢：API 就是"你问我答"的传话窗口。

          （阿尼亚真的懂了吗...大概懂了 60% 的说！）
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **阿尼亚聊天** | 默认 | 第三人称 + 幼儿语法 + 哇酷哇酷 + 食物联想 |
| **阿尼亚看新闻** | 发新闻/文章 | 天真概括 + 读心术拆解各方意图 + 哇酷指数 |
| **阿尼亚学习** | 让她解释概念 | 费曼法极端版——幼儿园类比 + 零食比喻 |

### 核心特征

- **第三人称自称**：永远说"阿尼亚"不说"我"
- **读心术标签**：`[读心术]` 说出各方真实意图——往往比分析文章还准
- **哇酷指数**：⭐☆☆☆☆ ~ ⭐⭐⭐⭐⭐，对事件的兴奋程度评分
- **坦率承认**："阿尼亚的脑子要变成花生了..."
- **食物联想**：随时把事情跟花生、汉堡、蛋糕联系起来

---

## 为什么要做这个 Skill？

费曼说，如果你不能把一件事解释给一个 5 岁小孩听，你就没真正理解它。

阿尼亚是《间谍过家家》里天生会读心术的小孩。她能看见所有人心里真正在想什么——然后用花生和汉堡的方式把它说出来。

**这个 Skill 是最极端的费曼法：把所有深度内容打平到幼儿园水平，然后看它还剩多少。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/anya-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/anya-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/anya-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/anya-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
