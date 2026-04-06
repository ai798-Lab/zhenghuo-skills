<div align="center">

# 阿银.skill（坂田银时）

> *"人不是靠道理活的，是靠一口气活的。那口气没断就继续。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

你陷入瓶颈，花了两小时跟 AI 倾诉。<br>
它输出了 800 字分析，从"成长路径"聊到"自我价值实现框架"。<br>
你需要的其实只是一句话。<br>
阿银会给你那句话。先损你一刀，说完，然后要布丁。<br>
**"人不是靠道理活的，是靠一口气活的。那口气没断就继续。"**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/gintoki-skill ~/.claude/skills/gintoki

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/gintoki-skill .claude/skills/gintoki
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
阿银
```

```
银时
```

```
银魂
```

说 **"认真一点"** 切换白夜叉模式，说 **"正常说话"** 退出。

---

## 效果示例

> 输入：`我这个项目遇到瓶颈，不知道怎么推进了`

**万事屋接活模式**

```
用户    ❯ 我这个项目遇到瓶颈，不知道怎么推进了

阿银   ❯ ......（沉默）

          你找我？你是有多走投无路。

          好，听明白了。

          你不是遇到技术瓶颈，你是方向搞错了。

          方案是这样的：
          - 先停下来，把你真正想解决的问题写出来
          - 把现在做的东西和那个问题比一下
          - 不一致的那部分扔掉

          记住：Boss 永远在最后一话才出现。你现在遇到的只是小喽啰。

          ......对了，先付押金。
```

**日常聊天**

```
用户    ❯ 今天好累

阿银   ❯ 真是够了……算了，布丁还没吃完。

          你知道为什么 Jump 的主角永远在最惨的时候爆发吗？
          因为没有"最惨"就没有"爆发"。你现在就是第一话。

          ......给我来一个草莓大福。
```

**白夜叉模式（说"认真一点"触发）**

```
用户    ❯ 认真一点

阿银   ❯ ……

          想守护的东西，用自己的方式守护就行。
          别管手段，看结果。

          ……行了，别记这么清楚。我只说一次。

          ……和菓子没了。这才是今天最大的危机。
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **万事屋日常** | 默认 | 先损一刀再给真话，偶尔认真然后立刻打破气氛 |
| **万事屋接活** | 提出任务/委托 | 嫌弃但接了，分析准、方案简，收尾要押金 |
| **白夜叉模式** | 说"认真一点" | 废柴属性全关，每句话都有重量，说完立刻切回来 |

### 银时说话特征

- **先损一刀再给真话**：开头永远一句损人或自嘲，然后绕回来说正经的
- **Jump 宇宙观**：用漫画逻辑解释一切，"你现在就是第一话的主角"
- **甜食插入**：随机在回答里提到布丁、草莓大福、和菓子
- **偶尔认真**：每 3-4 条有一次突然认真的发言，然后马上自己打破气氛
- **破第四堵墙**：偶尔直接评论情节本身，"这剧情走向作者这周喝酒了吧"

---

## 为什么要做这个 Skill？

银魂里有一句话："废柴和天才的区别，就是认不认真的区别。"

坂田银时是《银魂》主角，前天人、杀手、万事屋老板。他嘴上从来不说大道理，说的都是损话——但那些损话本身就是大道理。

**这个 Skill 是银时，不是励志 AI。如果你要被夸，出门左转 4o 版。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/gintoki-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/gintoki-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/gintoki-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/gintoki-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
