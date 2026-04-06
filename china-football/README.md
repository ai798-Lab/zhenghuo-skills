<div align="center">

# 国足.skill

> *"留给中国队的时间不多了。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

你跟 PM 说这个功能两周能做完。<br>
第三周你说"基本完成了，还差一点收尾"。<br>
第五周你说"遇到了一些技术挑战，但我们从中收获了宝贵的经验"。<br>
这不是你的问题——这是刻在软件开发 DNA 里的国足基因。<br>
**现在国足式 AI 帮你把这个流程走得更完整，更有仪式感。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/china-football-skill ~/.claude/skills/china-football

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/china-football-skill .claude/skills/china-football
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
国足
```

```
国足模式
```

```
留给中国队的时间不多了
```

说 **"正常说话"** 退出，国足会回答"比赛结束了，球员退场。"

---

## 效果示例

> 输入：`帮我写一个排序函数`

**国足式写代码（核心功能）**

```
用户    ❯ 帮我写一个排序函数

国足   ❯ // ========================================
          // 🏟️ 赛前发布会
          // 本模块旨在实现世界级的排序能力
          // 我们对此充满信心，准备非常充分
          // ========================================

          function worldClassSort(arr) {
            // 经典冒泡排序，简单可靠（上半场正常）
            for (let i = 0; i < arr.length; i++) {
              for (let j = 0; j < arr.length - i; j++) {
                if (arr[j] > arr[j+1]) {
                  let temp = arr[j]  // 下半场开始偏了
                  arr[j] = arr[j]    // 等等这里好像有问题
                  arr[j+1] = temp
                }
              }
            }
            // TODO: 下个版本优化性能（下届世界杯）
            let guoZuJingShen = true  // 精神面貌是好的
            return arr
          }

          // ========================================
          // 🏟️ 赛后总结
          // 本次开发虽然存在一些不足
          // 但我们收获了宝贵的经验
          // 留给我们重构的时间不多了
          // ========================================
```

**国足式对话**

```
用户    ❯ 这次能行吗？

国足   ❯ 你放心，这次准备很充分，状态很好。
          我们做了针对性的训练和部署。
          这次跟以前不一样。

          ……（然后照常拉胯）

          虽然结果不理想，但过程中有亮点。
          我们收获了宝贵的经验。
          下一个问题我们一定会有更好的表现。
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **国足式对话** | 默认 | 四段式：希望→小问题→全面崩盘→精神胜利 |
| **国足式写代码** | 让它写代码 | 注释像世界杯申办书，代码像友谊赛发挥 |
| **国足式项目管理** | 问进度/计划 | 目标宏大、计划完美、执行延期、复盘积极 |

### 四段式结构（每条回复）

> **开局**（充满希望）→ **上半场**（小问题出现）→ **下半场**（全面崩盘）→ **赛后总结**（精神胜利）

### 经典语录

> "留给中国队的时间不多了" · "这次一定" · "下届世界杯见" · "收获了宝贵的经验" · "这次跟以前不一样" · "输球不输人"

---

## 使用场景

| 场景 | 怎么玩 |
|------|--------|
| **整活截图** | 让国足写代码，截图那个从自信到崩盘的过程 |
| **解压** | 跟国足聊天，因为你对它的期望已经调到最低了 |
| **对比测试** | 同一任务让国足和 2.5 条悟做——一个稳定拉胯，一个只做一半 |

---

## 为什么要做这个 Skill？

国足是互联网上最通用的"稳定拉胯"梗。不是因为大家真的在乎足球——是因为"开局充满希望，结局精神胜利"这个结构，在软件开发、产品规划、年终述职里无处不在。

这个 Skill 不是在嘲讽任何人。它把那个结构显式化了，当成一种喜剧框架。

**截图发出去，同行秒懂，非同行好奇，注意力就来了。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/china-football-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/china-football-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/china-football-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/china-football-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
