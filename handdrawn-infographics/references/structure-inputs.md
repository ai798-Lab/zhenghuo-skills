# 新结构输入

九类新结构沿用 `build.py brief.json --out 交付`。通用字段 id/kind/title/mode/subtitle/source/note/模式与输出尺寸设置保持不变；改用 `data` 表达关系，不能同时传 `items` 或 `columns`。

完整可运行输入在 `assets/examples/structures.json`。先据正文选择结构，再填关系；下列限制用于保证可读性，不是关系定义。超过限制应拆图或定制，不能丢节点、缩字或悄悄换回列表。

可选 `intent` 写读者问题，`selection_reason` 写选型原因；它们进入 manifest，不显示在图里。

## 正文手绘图标

各结构的 `title` / `lines` 内容块支持 `icon`；tree 的 nodes、decision 的 question/branches、swimlane 的 events、layers 的 layers、funnel 的 stages 都可填写。venn 的 left/right/intersection 也支持，其中左右图标画在各自独有区域。table 使用 `column_icons: ["folder", "messages-square"]` 为两个比较方案指定图标。

可用图标：copy、messages-square、search、book-open、puzzle、chart-line、timeline、download、rocket、external-link，以及 folder、checklist。必须按内容选择，不能每个节点都随手放拼图。旧输入未填时会使用有限的标题关键词匹配作兼容兜底，正式制作优先显式指定。

示例：`{"title":"核实依据","lines":["确认来源与事实"],"icon":"checklist"}`。图标会参与占位计算；窄节点放在标题上方，宽节点放在标题右侧，正文仍保留原字号。未知图标会报错，不会悄悄替换或删除。

所有文本支持 `\n` 显式换行。自动折行按字形宽度处理，不能保证中文短语完整；菱形、树节点等窄区域先按语义安排短行，再检查成图。例如判断标题可写 `"稿件\n关键事实\n已核实吗？"`。不能用缩小字号来容纳长段原文。

## tree：父子归属

```json
{"nodes":[
  {"id":"root","title":"内容制作"},
  {"id":"text","parent":"root","title":"文字","lines":["组织表达"]},
  {"id":"visual","parent":"root","title":"配图","lines":["解释关系"]}
]}
```

一个根、唯一 id、存在的 parent、无环且连通。每个子节点只有一个父节点；多父关系用概念图定制。书籍最多四片叶子，手机最多三片，过多则拆子树；可有多层。

## radial：一个中心的多侧面

```json
{"center":{"title":"好内容"},"items":[
  {"title":"问题","lines":["要回答什么"]},
  {"title":"证据","lines":["有什么依据"]},
  {"title":"表达","lines":["怎样讲清楚"]}
]}
```

3–6 个短分支，中心必须简短。一层展开，没有默认方向和先后；不是循环，也不是通用网络。

## matrix：两个维度交叉

```json
{"x":{"title":"实施成本","low":"低","high":"高"},
 "y":{"title":"预期影响","low":"低","high":"高"},
 "quadrants":{
  "tl":{"title":"优先尝试","lines":["低成本，高影响"]},
  "tr":{"title":"重点规划","lines":["高成本，高影响"]},
  "bl":{"title":"顺手改进","lines":["低成本，低影响"]},
  "br":{"title":"谨慎投入","lines":["高成本，低影响"]}
 }}
```

tl/tr/bl/br 分别左上、右上、左下、右下。x 从左到右增加，y 从下到上增加。仅定性四象限分类；实际散点位置必须另用真实数据绘制。

## decision：显式条件

```json
{"question":{"title":"事实已核实？"},"branches":[
 {"label":"是","title":"进入写作","lines":["按确认材料展开"]},
 {"label":"否","title":"补充查证","lines":["寻找原始来源"]}
]}
```

一个判断点，2–3 个有标签的结果，手机两支。分支标签不得相同。多级判断、回路、多个起点等不能强行套此简化模式。

## swimlane：按责任归属串联

```json
{"lanes":["作者","AI 助手"],"events":[
 {"lane":"作者","title":"提出问题","lines":["明确目标"]},
 {"lane":"AI 助手","title":"整理草稿","lines":["保留来源"]},
 {"lane":"作者","title":"确认判断","lines":["人工审核"]}
]}
```

lanes 为 2–3 个不同角色，手机两列；events 为 2–8 个按实际顺序排列的步骤，每项指向已存在角色。相邻 events 直接连接，**只用于顺序交接**。并行、返工或复杂跳转需要显式图连接的定制版。

## layers：结构层次

```json
{"layers":[
 {"title":"应用层","lines":["文章、课程、报告"]},
 {"title":"方法层","lines":["研究、组织、表达"]},
 {"title":"基础层","lines":["资料、工具、经验"]}
]}
```

2–5 层，数组顺序即从上到下。没有默认因果箭头，也不把层的面积当作份额。

## funnel：逐步筛选的定性示意

```json
{"schematic":true,"stages":[
 {"title":"收集","lines":["收集可能线索"]},
 {"title":"筛选","lines":["保留相关内容"]},
 {"title":"核实","lines":["确认可靠材料"]}
]}
```

3–5 层，必须显式 schematic=true，图下自动标明宽度不是人数/转化率。真实转化数量应按数据绘制比例条形或另写定量漏斗，不能传数值后用固定宽度替代。

## venn：两集合的独有项与交集

```json
{"left":{"title":"已核实","only":["暂不相关"]},
 "right":{"title":"与主题相关","only":["尚未核实"]},
 "intersection":{"title":"优先采用","lines":["相关且已核实"]}}
```

only 是仅该集合独有的区域文字，intersection 是同时满足两者。图会标注面积不表数量。解释太长会拒绝，避免把小字塞进交集；可外移说明或改对照表。

## table：同维度对照

```json
{"columns":["方案 A","方案 B"],"rows":[
 {"dimension":"目标","values":["快速查阅","完整解释"]},
 {"dimension":"形式","values":["短清单","结构图加文字"]}
]}
```

两种方案，1–8 个比较维度；每行必须两份值。缺失数据应如实写“未提供”，不能擅自给出有利值。表格结构优先于两个彼此独立的长面板。
