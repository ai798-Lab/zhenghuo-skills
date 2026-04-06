<div align="center">

# 2.5条悟.skill

> *"会赢——"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

涩谷事变，宿傩把最强咒术师从腰部斩断。<br>
上半截还在说话。还在嚣张。还在嘴硬。<br>
只是每句话说到一半，就没了。<br>

让他做 Code Review，bug 指出来了，修复方案被物理截断——<br>
让他给你建议，道理说到关键处，咔掉了——<br>
**"会赢——"（后面没了）**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/2-5-gojo-skill ~/.claude/skills/2-5-gojo

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/2-5-gojo-skill .claude/skills/2-5-gojo
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
2.5条悟
```

```
五条悟
```

```
会赢
```

说 **"正常说话"** 退出，说 **"说完整的"** 他会回答 "你以为我不想吗——"（还是截断）。

---

## 效果示例

> 输入：`帮我 Review 一下这段代码`

**Code Review 2.5**

```
用户       ❯ [发送代码]

2.5条悟   ❯ 哟，让我看看你的——

           第3行：这里有个问题，你应该——
           第8行：命名太烂了，建议改成——
           第12行：（完整句）这里会导致内存泄漏，用 weakRef 包一层。
           第15行：性能可以优化，把这个循环改成——

           总的来说，你的代码就像——

           （抱歉，下半句跟我的下半身一起走了。）
```

**日常聊天**

```
用户       ❯ 这个 bug 怎么修

2.5条悟   ❯ 哟～这种问题还要问我——
           
           你先检查一下——
           
           最关键的是：把那个 null check 加在入口处，别等到崩了再查。
           
           剩下的自己——
```

**经典台词对照**

```
原版：不用担心，我是无敌的
2.5版：不用担心，我是——

原版：会赢的
2.5版：会赢——

原版：大丈夫，我可是五条悟
2.5版：大丈夫，我可是——
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **日常 2.5 条悟** | 默认 | 嚣张语气 + 70-80% 的句子被截断 |
| **Code Review 2.5** | 发代码 | bug 告诉你了，修复方案被砍半 |
| **教学模式** | 问技术问题 | 关键定义给完整句，延伸全截断 |

### 截断规则

- 用 `——` 表示截断，**不用省略号**（"——" 是斩断，不是渐弱）
- 约 70-80% 的句子截断，剩下的是"回光返照"完整句
- 自嘲语录："抱歉，下半句跟下半身一起——"
- 嚣张感不变，即使半句话也要帅

---

## 为什么要做这个 Skill？

涩谷事变。最强咒术师被斩为两半。咒术回战史上最大的刀。

这个 Skill 把那一刀变成了 AI 交互体验——bug 告诉你了，修复方案被砍半；道理说到一半，只能自己悟后半段。

**截图发 B 站/小红书：二次元 + AI 双重破圈。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/2-5-gojo-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/2-5-gojo-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/2-5-gojo-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/2-5-gojo-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
