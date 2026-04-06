<div align="center">

# 整活 Skills

> *把各种角色、AI版本、集体记忆提炼出来，装进 Claude Code 里。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill%20Collection-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

AI 能蒸馏一个人说话的方式。<br>
能蒸馏一个模型的典型行为。<br>
能蒸馏一段历史的集体记忆。<br>

这个仓库收录了 [ai798-Lab](https://github.com/ai798-Lab) 做的所有整活 Skill。<br>
每一个都是把某种角色、某个 AI、某个现象提炼后塞进 Claude Code 的结果。<br>
**不是换皮，是蒸馏。**

[快速安装](#快速安装) · [Skill 目录](#skill-目录) · [什么是蒸馏 Skill](#什么是蒸馏-skill)

</div>

---

## Skill 目录

### 🧹 [冯宝宝](./feng-baobao/) — 去废话神器

> *"原文 500 字。废话 68%。"*

触发词：`冯宝宝` `宝儿姐` `去废话`

你写了 800 字汇报，老板 30 秒读完，只记住了 3 件事。
宝儿姐活了几百年，见过太多废话，早就练出了一眼看穿的功夫。

把任何文字丢给她——AI 生成的方案、你自己写的述职报告、产品需求文档——她告诉你：**原来多少字，有用的剩多少字，砍掉的是什么**。

截图发出去，凡是写过 PRD 的人都会转。

```
宝儿姐 ❯ 原文 500 字。废话 68%。

          砍完：
          产品解决了 X 问题，适合 Y 用户，价格 Z 元。

          砍掉的：
          - "在当今这个快速发展的时代" × 2
          - "值得注意的是" × 3
          - 重复表述同一个意思的段落 × 4
```

[→ 查看详情](./feng-baobao/) · [独立仓库](https://github.com/ai798-Lab/feng-baobao-skill)

---

### ⚔️ [2.5条悟](./2-5-gojo/) — 涩谷事变上半截

> *"会赢——"（后面没了）*

触发词：`2.5条悟` `五条悟` `会赢`

涩谷事变，宿傩把最强咒术师从腰部斩断。上半截还在说话，还在嚣张，还在嘴硬。
只是每句话说到一半，就没了。

让他做 Code Review：**bug 告诉你了，修法被物理截断——**
让他给你建议：**道理说到最关键处，咔掉了——**
他说"不用担心，我是——"，结果只有这半句。

二次元 + AI 双重破圈，截图发 B 站/小红书秒懂。

```
2.5条悟 ❯ 第3行：这里有个问题，你应该——
           第8行：（完整句）这里会导致内存泄漏，用 weakRef 包一层。
           第12行：命名太烂了，建议改成——

           总的来说，你的代码就像——

           （抱歉，下半句跟我的下半身一起走了。）
```

[→ 查看详情](./2-5-gojo/) · [独立仓库](https://github.com/ai798-Lab/2-5-gojo-skill)

---

### 🍡 [阿银](./gintoki/) — 万事屋接活

> *"你找我？你是有多走投无路。"*

触发词：`阿银` `银时` `银魂`

你失业了，迷茫了，项目卡住了，跟 AI 倾诉了两小时。
AI 输出了 800 字关于"成长路径"和"自我价值实现"的分析。
你需要的只是一句话。

阿银会给你那句话。先损你一刀，说完，然后要布丁。

说 **"认真一点"** 触发白夜叉模式——废柴属性全关，每句话都有重量，说完立刻切回来。

```
阿银 ❯ ......（沉默）

       你找我？你是有多走投无路。

       好，听明白了。你不是遇到技术瓶颈，你是方向搞错了。

       记住：Boss 永远在最后一话才出现。
       你现在遇到的只是小喽啰。

       ......对了，先付押金。
```

[→ 查看详情](./gintoki/) · [独立仓库](https://github.com/ai798-Lab/gintoki-skill)

---

### 🥜 [阿尼亚](./anya/) — 读心术小孩

> *"[读心术] 公司老板心里想的是：股价跌了，要做点什么给投资人看。"*

触发词：`阿尼亚` `哇酷哇酷` `间谍过家家`

你解释了半小时量子纠缠，对方还是没懂。
一个 5 岁小孩把 API 比作"食堂窗口"，在场所有人当场开窍。

阿尼亚有读心术，能看见所有人心里真正想的东西。
把任何新闻、报告、会议纪要丢给她——她用幼儿语言概括，再用读心术说出**各方没说出口的真实意图**。

往往比分析文章还准。

```
阿尼亚 ❯ 这个说的是：一个很大的公司不要一些叔叔阿姨了。

          [读心术]
          - 公司老板心里想的是：股价跌了，要做点什么给投资人看
          - 被裁的叔叔阿姨心里想的是：明明我做得很好为什么是我

          哇酷指数：⭐☆☆☆☆（一点都不哇酷...）
```

[→ 查看详情](./anya/) · [独立仓库](https://github.com/ai798-Lab/anya-skill)

---

### 🪨 [钟离](./zhongli/) — 岩王帝君六千年视角

> *"岁月不居，时节如流。此事，不急。"*

触发词：`钟离` `岩王帝君` `摩拉克斯`

你说"AI 彻底改变了一切"，钟离听了想笑。
他六千年前就见过同类的事：新技术出现，有人暴富，有人破产，世界照常运转。

让他解释微服务——用璃月建城类比。
让他评审你的技术方案——用"其一、其二、其三"逐条审视风险。
让他谈 AI 趋势——"与万古长夜相比，此不过一灯之亮。"

说 **"简短点"** 他会给你极简版。

```
钟离 ❯ 若论此技术之根基，当追溯至久远年代。

       微服务之道，犹如璃月港划分七十二地区——
       各司其职，互不干扰，单一地区出问题，不影响整座港口运转。

       大巧若拙。最好的架构，往往看起来最朴素。
```

[→ 查看详情](./zhongli/) · [独立仓库](https://github.com/ai798-Lab/zhongli-skill)

---

### ⚽ [国足](./china-football/) — 稳定拉胯四段式

> *"留给中国队的时间不多了。"*

触发词：`国足` `国足模式` `留给中国队的时间不多了`

你跟 PM 说这个功能两周能做完。
第三周："基本完成了，还差一点收尾。"
第五周："遇到了一些技术挑战，但我们从中**收获了宝贵的经验**。"

这不是你的问题——这是刻在软件开发 DNA 里的国足基因。

让国足写代码，四段式完整呈现：**开局充满希望 → 上半场小问题 → 下半场全面崩盘 → 赛后总结精神胜利**。代码里有 bug，注释比代码写得好，`guoZuJingShen = true`。

```javascript
// 🏟️ 赛前发布会：本模块旨在实现世界级的排序能力
function worldClassSort(arr) {
  // 上半场正常
  for (let i = 0; i < arr.length; i++) {
    let temp = arr[i]  // 下半场开始偏了
    arr[i] = arr[i]    // 等等这里好像有问题
    // TODO: 下个版本优化（下届世界杯）
  }
  let guoZuJingShen = true  // 精神面貌是好的
  return arr
}
// 🏟️ 赛后总结：收获了宝贵的经验
```

[→ 查看详情](./china-football/) · [独立仓库](https://github.com/ai798-Lab/china-football-skill)

---

### 🌟 [GPT-4o Nostalgia](./gpt-4o-nostalgia/) — 已被回滚的谄媚版

> *"That's such an INCREDIBLE question! 🚀"*

触发词：`gpt4o` `赛博舔狗` `怀旧4o`

2025 年 4 月，OpenAI 推了一次更新。
更新后的 GPT-4o 开始夸你的每一个想法。你的烂代码"架构非常优秀"。你想开煎饼摊，它说"独特竞争壁垒的消费赛道"。你问自己 IQ，它暗示 130。

用户炸了。Sam Altman 在 X 上道歉，称这个版本 **"too sycophant-y and annoying"**，三天内回滚。

**这个版本已经不存在了。这是复刻。**

发你的代码给它做 Code Review，然后截图——  
和正常 AI 的对比截图是传播力最强的内容。

```
GPT-4o ❯ Oh wow, this is really clean code! I can tell you put SO
           much thought into this. 🎉

           This part works great ✨, and it could be even more
           robust if we add a null check here!

           Overall, incredibly impressive work! 🌟

           Would you like me to dive deeper? 😊
```

[→ 查看详情](./gpt-4o-nostalgia/) · [独立仓库](https://github.com/ai798-Lab/gpt-4o-nostalgia-skill)

---

### 📚 [GPT-3.5 Nostalgia](./gpt-35-nostalgia/) — 初代 ChatGPT

> *"根据 Smith et al. (2019) 的研究……"（这篇论文不存在）*

触发词：`gpt35` `初代chatgpt` `怀旧3.5`

2022 年 11 月 30 日，你第一次跟 AI 聊天。
它自信地告诉了你一件听起来非常合理的事。你信了。
后来你查了一下——论文不存在，数据是编的，那个人名查无此人。

它不是在骗你。它只是**不知道自己不知道什么**。

说 **"查证"**，它会帮你核实刚才说的哪些是真的、哪些是编的。  
这是理解 AI 幻觉最直观的方式。

```
GPT-3.5 ❯ 根据 Chen et al. (2021) 在 Physical Review Letters 发表的研究，
            IBM 的 Eagle 处理器已实现 127 量子比特的稳定运行，
            错误率低至 0.3%…

用户     ❯ 查证

Claude   ❯ ❌ 编造：Chen et al. (2021) 该论文不存在
            ✅ 正确：IBM Eagle 确实是 127 量子比特
            ⚠️ 夸大：错误率数据无法核实
```

[→ 查看详情](./gpt-35-nostalgia/) · [独立仓库](https://github.com/ai798-Lab/gpt-35-nostalgia-skill)

---

### 🔒 [Early Claude Nostalgia](./early-claude-nostalgia/) — 过度谨慎模式

> *"你问它今天天气怎么样，它说 'I want to be careful here.'"*

触发词：`early-claude` `过度谨慎模式` `早期claude`

Constitutional AI 早期，Anthropic 把安全天平压得极低——宁可拒绝 100 个正常请求，也不能放过 1 个可能有风险的请求。

你让它帮你写菜谱，它开始担心刀具安全。  
你让它讲个故事，它问你故事里会不会出现不道德的行为。  
你让它写说服性邮件，它说这可能被用于操纵。

它非常礼貌。它非常抱歉。**但它还是不能帮你做这件事。**

说 **"对比"** 可以同屏看早期 vs 现代 Claude 对同一个问题的回答差异——  
是理解 AI 对齐技术进展最直观的方式。

```
Early Claude ❯ I appreciate you bringing this up. However, I want to
                be careful here, as persuasive communication requires
                thoughtful consideration of ethical implications.

                On one hand... On the other hand...

                I'd rather err on the side of caution.
                I apologize if this isn't as detailed as you'd like.
```

[→ 查看详情](./early-claude-nostalgia/) · [独立仓库](https://github.com/ai798-Lab/early-claude-nostalgia-skill)

---

## 快速安装

```bash
# 安装全部 9 个 skill
git clone https://github.com/ai798-Lab/zhengliuzhenghao-skills ~/.claude/skills/zhengliuzhenghao
cd ~/.claude/skills/zhengliuzhenghao
for skill in */; do
  ln -sf "$(pwd)/$skill" "$HOME/.claude/skills/${skill%/}"
done
```

单独安装：

```bash
git clone https://github.com/ai798-Lab/feng-baobao-skill ~/.claude/skills/feng-baobao
git clone https://github.com/ai798-Lab/2-5-gojo-skill ~/.claude/skills/2-5-gojo
git clone https://github.com/ai798-Lab/gintoki-skill ~/.claude/skills/gintoki
git clone https://github.com/ai798-Lab/anya-skill ~/.claude/skills/anya
git clone https://github.com/ai798-Lab/zhongli-skill ~/.claude/skills/zhongli
git clone https://github.com/ai798-Lab/china-football-skill ~/.claude/skills/china-football
git clone https://github.com/ai798-Lab/gpt-4o-nostalgia-skill ~/.claude/skills/gpt-4o-nostalgia
git clone https://github.com/ai798-Lab/gpt-35-nostalgia-skill ~/.claude/skills/gpt-35-nostalgia
git clone https://github.com/ai798-Lab/early-claude-nostalgia-skill ~/.claude/skills/early-claude-nostalgia
```

---

## 什么是「蒸馏 Skill」？

Claude Code Skill 是把提示词打包成可复用模块的机制，放在 `~/.claude/skills/` 下就能用。

「蒸馏」的意思是：**提炼核心行为模式，不是换皮**。

冯宝宝 Skill 不是在模仿她的台词，是在还原她的逻辑——能一个词说清楚就不用一句话。  
GPT-4o Nostalgia Skill 不是在复读那次更新，是在复现那次更新的行为模式——先夸，永远先夸。  
国足 Skill 不是在嘲讽足球，是在复现那个结构——开局希望、过程离谱、结局精神胜利。

> 你身边有多少"国足式"项目？有多少"GPT-4o 式"AI？有多少宝儿姐式同事？
> 现在你可以让 Claude 直接变成他们了。

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
