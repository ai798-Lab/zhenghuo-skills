# 信息结构资料与设计依据

检索核对日期：2026-09-27。以下是第一方资料或专业方法说明；没有复制网站模板、海报或原文进本技能。新样图为本地原创示例。

## 常见信息图分类

- [Visme：13 Types of Infographics](https://visme.co/blog/types-of-infographics/)：覆盖过程、对比、层级、解剖、地理等常见用途，也把交互性纳入分类。用于提醒信息图远不止步骤列表；不把这 13 类视为严格互斥的结构标准。
- [Venngage：9 Types of Infographics](https://venngage.com/blog/9-types-of-infographic-template/)：另一种按内容目的整理的实用分类。与 Visme 的数量差异表明，这类数字代表各家组织模板的方法，而非本技能必须照搬的固定类别数。

## 关系图解

- [NN/g：Cognitive Maps, Mind Maps, and Concept Maps](https://www.nngroup.com/articles/cognitive-mind-concept/)：思维导图围绕主题向外形成树；概念图能够表现带关系词的多重连接。对本技能的影响：中心展开、父子归属、多对多关系分别选择布局。
- [Lucidchart：Flowchart Tutorial](https://app.lucid.co/diagram/flowchart/tutorial)：流程符号承担不同语义，判断分支应与普通处理步骤区分。用于 decision 的菱形判断点和显式分支标签。
- [Lucidchart：Swimlane Diagram](https://app.lucid.co/diagram/swimlane/how-to-create-a-swimlane-diagram)：通过参与者与顺序步骤的结合呈现责任和交接。用于 swimlane 的角色列，而非只更换节点颜色。
- [ASQ：Fishbone](https://asq.org/quality-resources/fishbone)：把某个问题的可能原因按类别整理。用于因果类选型规则；识别潜在原因并不等于已经证实原因。

## 图表和可视化选型

- [FT Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md)：从偏差、相关、排序、分布、时间变化、整体与部分、大小、空间和流动等问题选择数据图。用于需要真实数据的图表分流；不能把数值分析全部装入文字卡片。
  官方仓库也提供 [简体中文 PDF](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/Visual-vocabulary-cn-simplified.pdf)，适合查阅数据图类型；此处只链接，没有将海报复制进 Skill。
- [The Data Visualisation Catalogue：按功能查找](https://datavizcatalogue.com/search.html)：以“要让读者看见什么”为入口。其 [树图](https://datavizcatalogue.com/methods/tree_diagram.html)、[网络图](https://datavizcatalogue.com/methods/network_diagram.html)、[Venn 图](https://datavizcatalogue.com/methods/venn_diagram.html)分别对应层级、连接与集合逻辑，是不同关系，不是同一模板的皮肤变化。

## 本项目的判断

本技能采用“信息关系 → 空间构图 → 视觉样式”三层决策。这是针对当前问题整理的工作方法，不宣称是上述某家机构的原文标准。

上一版的局限来自实现：五个 kind 大多走同一个卡片循环；同时，“每行最多两块、手机单列”被写成了过宽的规则。新版保留阅读字号和品牌视觉，解除与具体关系冲突的布局限制，并提供九个独立结构渲染器。

定量图和复杂关系仍需专门设计，内置模板覆盖不了所有知识结构。结构库同时明确“内置可运行”和“按真实关系定制”，避免用一张普通卡片图冒充复杂关系图。
