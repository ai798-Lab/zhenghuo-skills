<div align="center">

# 蒸馏整活 Skills

> *把各种角色/AI/现象的精髓提炼出来，装进 Claude Code 里。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill%20Collection-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

AI 能蒸馏一个人说话的方式。<br>
能蒸馏一个模型的典型行为。<br>
能蒸馏一段历史的集体记忆。<br>

这个仓库收录了 ai798-Lab 做的所有整活 Skill——<br>
每一个都是把某种角色、某个 AI、某个现象提炼后塞进 Claude Code 的结果。<br>
**有用的、有趣的、有梗的，都在这里。**

</div>

---

## Skill 列表

| Skill | 核心梗 | 触发词 | 独立仓库 |
|-------|--------|--------|---------|
| [冯宝宝](./feng-baobao/) | 国漫顶流去废话神器，四川话，砍完告诉你废了多少 | `冯宝宝` `宝儿姐` `去废话` | [feng-baobao-skill](https://github.com/ai798-Lab/feng-baobao-skill) |
| [2.5条悟](./2-5-gojo/) | 涩谷事变上半截，每句话说到一半就没了—— | `2.5条悟` `五条悟` `会赢` | [2-5-gojo-skill](https://github.com/ai798-Lab/2-5-gojo-skill) |
| [阿银](./gintoki/) | 废柴银时，先损你一刀再给大道理，然后要押金 | `阿银` `银时` `银魂` | [gintoki-skill](https://github.com/ai798-Lab/gintoki-skill) |
| [阿尼亚](./anya/) | 读心术小孩，用花生和汉堡解释所有技术概念 | `阿尼亚` `哇酷哇酷` | [anya-skill](https://github.com/ai798-Lab/anya-skill) |
| [钟离](./zhongli/) | 活了六千年的岩王帝君，用璃月历史类比微服务 | `钟离` `岩王帝君` | [zhongli-skill](https://github.com/ai798-Lab/zhongli-skill) |
| [国足](./china-football/) | 稳定拉胯四段式：希望→问题→崩盘→收获经验 | `国足` `留给中国队的时间不多了` | [china-football-skill](https://github.com/ai798-Lab/china-football-skill) |
| [GPT-4o Nostalgia](./gpt-4o-nostalgia/) | Sam Altman 亲自道歉回滚的谄媚版，赛博舔狗复刻 | `gpt4o` `赛博舔狗` | [gpt-4o-nostalgia-skill](https://github.com/ai798-Lab/gpt-4o-nostalgia-skill) |
| [GPT-3.5 Nostalgia](./gpt-35-nostalgia/) | 初代 ChatGPT，自信编论文引用，格式完美查无此文 | `gpt35` `初代chatgpt` | [gpt-35-nostalgia-skill](https://github.com/ai798-Lab/gpt-35-nostalgia-skill) |
| [Early Claude Nostalgia](./early-claude-nostalgia/) | 2023 年初的过度谨慎版，菜谱也能联想到刀具安全 | `early-claude` `过度谨慎模式` | [early-claude-nostalgia-skill](https://github.com/ai798-Lab/early-claude-nostalgia-skill) |

---

## 快速安装（全部）

```bash
# 安装全部 9 个 skill（全局）
git clone https://github.com/ai798-Lab/zhengliuzhenghao-skills ~/.claude/skills/zhengliuzhenghao

# 然后把每个子目录软链接到 skills 根目录
cd ~/.claude/skills/zhengliuzhenghao
for skill in */; do
  ln -sf "$(pwd)/$skill" "$HOME/.claude/skills/${skill%/}"
done
```

或者单独安装你需要的：

```bash
# 只装冯宝宝
git clone https://github.com/ai798-Lab/feng-baobao-skill ~/.claude/skills/feng-baobao

# 只装 2.5条悟
git clone https://github.com/ai798-Lab/2-5-gojo-skill ~/.claude/skills/2-5-gojo
```

---

## 什么是「蒸馏 Skill」？

Claude Code Skill 是一种把提示词打包成可复用模块的机制。
放在 `~/.claude/skills/` 或项目的 `.claude/skills/` 下就能用。

「蒸馏」的意思是：把某个角色、某个 AI 版本、某种现象的核心行为模式提炼出来，用 SKILL.md 定义，让 Claude 扮演得足够准确。

> 不是换皮，是提炼。
> 冯宝宝 Skill 不是在模仿她的台词，是在还原她的逻辑：能一个词说清楚就不用一句话。

---

## Star History

<a href="https://star-history.com/#ai798-Lab/zhengliuzhenghao-skills&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/zhengliuzhenghao-skills&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ai798-Lab/zhengliuzhenghao-skills&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ai798-Lab/zhengliuzhenghao-skills&type=Date" />
 </picture>
</a>

---

<div align="center">

MIT License © [ai798-Lab](https://github.com/ai798-Lab)

</div>
