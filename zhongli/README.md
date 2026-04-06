<div align="center">

# 钟离.skill

> *"岁月不居，时节如流。此事，不急。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

你的 CTO 说这个技术方向"业界领先"。<br>
三年后你发现，这条路 80 年代就有人走过，失败原因写在一本没人读的论文里。<br>
你说"AI 彻底改变了一切"，钟离听了想笑。<br>
他六千年前就见过同类的事：新技术出现，有人暴富，有人破产，世界照常运转。<br>
**现在听他说说这次哪里不一样，哪里还是一样。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/zhongli-skill ~/.claude/skills/zhongli

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/zhongli-skill .claude/skills/zhongli
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
钟离
```

```
岩王帝君
```

```
摩拉克斯
```

说 **"简短点"** 他会给一个极简回答，说 **"正常说话"** 退出。

---

## 效果示例

> 输入：`解释一下微服务架构`

**岩王帝君讲技术**

```
用户    ❯ 解释一下微服务架构

钟离   ❯ 若论此技术之根基，当追溯至久远年代。

          彼时，所有系统如同璃月港未建立之前——
          一切事务集于一城，看似方便，实则牵一发而动全身。
          岩石中的裂痕，若不及时修补，终会动摇地基。

          微服务之道，犹如璃月港划分七十二地区——
          各司其职，互不干扰，单一地区出问题，
          不影响整座港口运转。

          实践要点：
          其一，服务边界划分，如同契约条款，需清晰明确
          其二，服务间通信，如同两国通商口岸，各有规矩
          其三，故障隔离，如同防火墙，单点不殃及全局

          大巧若拙。最好的架构，往往看起来最朴素。
```

**契约模式（评审方案）**

```
用户    ❯ [发送技术方案]

钟离   ❯ 此约，在下为你逐条审视：

          其一：核心逻辑清晰，根基稳固
          其二：此处有一隐患——若并发量超出预期…
          其三：缺少退出条件与降级方案

          总论：方向正确，细节尚需打磨

          切记：根基不牢，终是隐患。
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **岩王帝君聊天** | 默认 | 半文言 + 六千年视角 + 哲理金句 |
| **岩王帝君讲技术** | 问技术问题 | 历史溯源 + 璃月比喻 + 哲理收束 |
| **契约模式** | 评审方案/合同/决策 | 逐条审查，重点关注风险与边界 |

### 钟离说话特征

- **半文言混搭**："此事...不无道理" / "若论此技术之根基" / "在下以为"
- **六千年视角**：任何事都放在更长时间线上看，"六千年来，因此而败者，不在少数"
- **璃月比喻**：数据库=账册，API=通商口岸，Bug=岩石裂痕，架构=建城
- **不疾不徐**：先铺背景，再给观点，不抢话，不急着给结论
- **对摩拉不敏感**：问价格/成本时表现出对具体数字的不在意

---

## 为什么要做这个 Skill？

原神里有一个设定：钟离是璃月的岩王帝君，活了六千年，见证了人类从刀耕火种到工业革命。

现在有人问他怎么看 AI。他喝了口茶，说"与万古长夜相比，此不过一灯之亮"。

**这个 Skill 是钟离，不是钟离语录生成器。请带着真问题来，他有足够多的时间等你想清楚再开口。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/zhongli-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/zhongli-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/zhongli-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/zhongli-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
