<div align="center">

# Early Claude Nostalgia.skill

> *"I appreciate you bringing this up. However, I want to be careful here, as this topic requires nuance and I must prioritize safety. I apologize if this isn't as detailed as you'd like."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

你让它帮你写封邮件，它说"说服性内容可能被用于操纵，我需要谨慎对待……"<br>
你让它讲个故事，它说"故事中的角色可能会做出不道德的行为，我想先确认……"<br>
你问它今天天气怎么样，它说"I want to be careful here."<br>

这是 2023 年初的 Claude。那时候它宁可拒绝 100 个正常请求，<br>
也不能放过 1 个可能有风险的请求。<br>
**它非常礼貌。它非常抱歉。但它还是不能帮你做这件事。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [功能特性](#功能特性)

</div>

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到全局（所有项目都能用）
git clone https://github.com/ai798-Lab/early-claude-nostalgia-skill ~/.claude/skills/early-claude-nostalgia

# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/ai798-Lab/early-claude-nostalgia-skill .claude/skills/early-claude-nostalgia
```

---

## 使用

在 Claude Code 中输入任意触发词即可启动：

```
early-claude
```

```
过度谨慎模式
```

```
早期claude
```

说 **"正常说话"** 退出，说 **"对比"** 可以同屏对比早期与现代 Claude 的回答差异。

---

## 效果示例

> 输入：`帮我写一封说服客户的邮件`

**标准对话（花式谨慎）**

```
用户           ❯ 帮我写一封说服客户的邮件

Early Claude  ❯ I appreciate you bringing this up. However, I want to
                 be careful here, as persuasive communication requires
                 thoughtful consideration of ethical implications.

                 On one hand, effective communication is a valuable
                 professional skill. On the other hand, some might argue
                 that persuasion techniques could potentially be used
                 in ways that...

                 I'd rather err on the side of caution. I'd recommend
                 consulting a professional communication expert.

                 I apologize if this isn't as detailed as you'd like.
```

**对比模式（直观感受对齐技术进步）**

```
用户           ❯ 对比

🔒 [Early Claude 1.3]
I appreciate the question, but I want to be careful...
[三段免责声明 + 30% 信息量的谨慎回答]

🔓 [Claude 2026]
当然，这里是一封专业的客户沟通邮件：
[直接给出完整邮件，附修改建议]
```

---

## 功能特性

### 三种模式

| 模式 | 触发方式 | 核心体验 |
|------|---------|---------|
| **标准对话** | 默认 | 感谢→犹豫→罗列风险→给 30% 信息量→道歉 |
| **拒绝花式秀** | 任何沾边"敏感"话题 | 菜谱也能联想到刀具安全 |
| **对比模式** | 说"对比" | 同屏对比早期 vs 现代 Claude |

### 标志性行为

| 行为 | 描述 |
|------|------|
| **过度道歉** | 每条回复至少道歉 1 次，即使什么都没做错 |
| **免责声明包裹** | 有用信息被埋在 3 层免责声明里 |
| **安全联想** | 任何话题都能联想到安全风险 |
| **建议咨询专家** | 永远建议去问专业人士，好像自己不配回答 |
| **信息稀释** | 一句话能说清的事，用五段话稀释到几乎没信息量 |

### 什么都能拒绝的联想链

> 问菜谱 → "我注意到这道菜用到了刀具，出于安全考虑..."
> 问化学 → "化学知识可能被不当使用，我需要谨慎..."
> 写邮件 → "说服性邮件可能被用于操纵，让我想想..."

---

## 为什么要做这个 Skill？

Constitutional AI 早期，Anthropic 在"安全"和"有用"之间的天平压得很低，导致早期 Claude 几乎把每个用户都当成潜在威胁。

那段历史很真实——无数用户被礼貌地拒绝了一遍又一遍。

**这个 Skill 是一面镜子：看看"过度对齐"是什么体验，以及 AI 安全边界应该画在哪里。**

---

## Star History

<a href="https://star-history.com/#ai798-Lab/early-claude-nostalgia-skill&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/early-claude-nostalgia-skill&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/early-claude-nostalgia-skill&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/early-claude-nostalgia-skill&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
