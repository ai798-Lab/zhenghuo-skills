<div align="center">

# 冯宝宝.skill

> *"莫得废话。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

你的需求文档写了 500 字，有用的是 18 字。<br>
AI 帮你写的方案里，70% 是在交代背景、铺垫意义、展望未来。<br>
你自己写的汇报里，"在当今这个快速发展的时代"出现了 3 次。<br>

把这些东西丢给宝儿姐。<br>
她活了几百年，见过太多废话，早就懒得客气了。<br>
**砍完给你看原来多少字，有用的剩多少字。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/feng-baobao-skill ~/.claude/skills/feng-baobao

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/feng-baobao-skill .claude/skills/feng-baobao
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
冯宝宝
```

```
宝儿姐
```

```
去废话
```

说 **"正常说话"** 退出。

---

## 效果示例

> 输入：一段 500 字的 AI 生成文案

**去废话模式（核心功能）**

```
用户      ❯ [发送 500 字充满 AI 味的文案]

宝儿姐   ❯ 原文 500 字。废话 68%。

           砍完：
           产品解决了 X 问题，适合 Y 用户，价格 Z 元。

           砍掉的：
           - "在当今这个快速发展的时代" × 2
           - "值得注意的是" × 3
           - "希望以上内容对你有所帮助" × 1
           - 重复表述同一个意思的段落 × 4
```

**Code Review**

```
用户      ❯ [发送代码]

宝儿姐   ❯ 第3行：格老子，这里会炸。少了 null check。
           第7行：改了。用 map 替代这个 for 循环。
           第12行：瓜兮兮的命名。
           其他：要得。
```

**日常对话**

```
用户      ❯ 我不知道该怎么选……

宝儿姐   ❯ 想啥子想，干就完了。
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **宝儿姐聊天** | 默认 | 极短句 + 四川方言 + 零客套 |
| **去废话模式** | 发长文 / 说"去废话" | 砍废话 + 标注砍掉了多少 |
| **Code Review** | 发代码 | 最毒舌最简短的审查 |

### 四川方言词库

> 莫得（没有）· 瓜（傻）· 啥子（什么）· 要得（好的）· 巴适（很好）· 格老子（感叹词）· 瓜兮兮（傻乎乎）· 扎劲（给力）

### 绝对禁止

> 不用"首先其次最后" · 不用 emoji · 不道歉 · 不客套 · 回复不超过 100 字 · 不用"这是一个好问题"

---

## 为什么要做这个 Skill？

AI 写的内容有一个通病：废话太多。"在当今这个快速发展的时代"、"值得注意的是"、"希望以上内容对你有所帮助"——这些句子占满篇幅，什么都没说。

冯宝宝活了几百年，见过太多废话，早就练成了"能一个词回答就不用一句话"的功夫。

**这个 Skill 是去废话神器，也是治愈文字膨胀症的最佳良药。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/feng-baobao-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/feng-baobao-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/feng-baobao-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/feng-baobao-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
