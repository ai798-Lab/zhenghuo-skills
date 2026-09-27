# 本地生成器

`scripts/build.py` 将 JSON 变为可编辑 SVG，并调用 `scripts/render.cjs` 导出 PNG，不联网。先按 [结构选型库](structure-library.md) 选结构；九类关系结构使用 [结构输入](structure-inputs.md)。复杂图用 `scripts/drawing.py` 原语另写布局。

## 环境与命令

需要 Python 3.10+ / fontTools / brotli、Node.js / sharp，以及 fontconfig（`fc-match`）。默认小赖字体随 Skill 提供，生成时无需先安装到系统。优先使用现有环境；Codex 桌面可通过 `load_workspace_dependencies` 查已提供的运行时，不默认联网安装，不索要 API Key。

```sh
python3 /absolute/path/to/handdrawn-infographics/scripts/build.py \
  /absolute/path/to/brief.json --out /absolute/path/to/交付
```

可选 `--font-regular PATH --font-bold PATH --node PATH --sharp-module PATH`。`--svg-only` 仅供调试，不能宣称双格式交付。默认拒绝覆盖同名产物；确认是本次产物后可用 `--overwrite`，不会清空目录。

默认直接读取 `assets/fonts/Xiaolai-Regular.ttf`，以真实 400 字重测量和导出。SVG 保留 `<text>`，嵌入当前图中文字的 WOFF2 子集；完整字体与 OFL 许可复制到输出的 `fonts/`，manifest 使用相对路径，可随输出目录一起移动。

如需其他字体，必须同时传入 `--font-regular` 和 `--font-bold`，同一家族、涵盖全部文字；单字重字体可重复传同一路径。CSS 字重读取字体本身的 OS/2 数据，不硬设为 700。显式自选字体不自动嵌入或分发，用户需确认其授权和跨机器依赖。

PNG 导出在进程内创建临时 fontconfig 配置，只读取指定字体目录，并在加载 sharp 前设置 `PANGOCAIRO_BACKEND=fontconfig`。`fc-match` 核对测量字体的实际文件；检查与 PNG 渲染使用同一后端，避免 macOS Core Text 忽略配置而悄悄回退。临时配置退出后清理，不修改系统字体或全局设置。仍须实看 PNG，不能仅凭字体匹配报告判断字形正确。[sharp 官方字体说明](https://sharp.pixelplumbing.com/install/#fonts)

Node 查找 PATH 与 Codex 本地缓存。sharp 尝试本地模块、环境变量 `SHARP_MODULE` 及 Codex 缓存；环境变更时显式指定路径。

## JSON 输入

```json
{
  "mode": "article",
  "figures": [{
    "id": "article-process", "kind": "steps",
    "title": "把一个观点写成文章",
    "subtitle": "从读者的问题出发，保留人工校对。",
    "source": "用户提供的写作流程",
    "items": [
      {"title": "确定读者", "lines": ["先写清读者的问题"], "icon": "messages-square"},
      {"title": "查证材料", "lines": ["保留来源与条件"], "icon": "search"},
      {"title": "人工校对", "lines": ["检查事实与表达"], "icon": "checklist", "human": true}
    ],
    "note": "保留可以回头修改的材料。"
  }]
}
```

必填 `figures` 非空数组；每图 `id`、`kind`、`title`。原有五种列表布局用 `items`（每项 title、lines 字符串数组）；九种关系布局用 `data`，两者不能混用。id 为中英文、数字、短横线或下划线，唯一且无路径，直接用作 SVG/PNG 文件名。

| 字段 | 可用值 |
| --- | --- |
| mode | article 默认 / book，可单图覆盖 |
| kind | items 类：steps / cards / compare / cycle / timeline；data 类：tree / radial / matrix / decision / swimlane / layers / funnel / venn / table |
| columns | 只用于 items 类的 1 / 2 列布局；不要传给 data 类，关系布局有自己的规则 |
| intent / selection_reason | 可选，读者问题与选型原因，仅写入制作记录 |
| label | 可选图号或栏目名，不自动产生书籍图号 |
| subtitle / note / source | 可选字符串；source 为真实来源说明 |
| items[].icon | 已附图标名，默认 puzzle |
| data 内的 icon / table.column_icons | 正文语义图标，具体位置见 [结构输入](structure-inputs.md)；不只生成标题装饰 |
| items[].label | 可选日期或阶段，时间轴优先使用，不替代 title |
| items[].human | true 使用浅橙，仍需保留人工操作文字 |
| print_width_mm | book 默认 144，改后核算字号 |
| dpi | book 默认 600；article 默认 144，屏幕以像素宽为准 |
| png_width | article 默认 1440；book 由物理宽与 dpi 计算 |

mode/print_width_mm/dpi/png_width 可在根级设置，单图优先。脚本拒绝未支持的字段，避免静默丢失连接。`assets/examples/demo.json` 为旧版兼容示例，`assets/examples/structures.json` 为九种新结构的完整输入。只取所需，不把演示内容混入用户交付。

## 输出

同一输出目录下：`SVG/<id>.svg`、`PNG/<id>.png`、`fonts/`（默认小赖完整字体、来源与 OFL 许可）、`manifest.json`、`render-report.json`、`NOTICE-sketchyicons.txt`。

manifest 记录生成时的文字边界、字号、来源、SVG 指纹与基础检查；render-report 记录 PNG 尺寸、字体匹配、当前 SVG 指纹与导出参数。两份报告不能代替实际看图。确认中文长标题、中英文混排、图标间距和阅读尺度；在临时副本修改文字再导出一次。

直接编辑 SVG 再 render 时，PNG 会更新，但生成时的文字边界不会自动重算。渲染器发现 SVG 指纹改变，就把 `layout_check` 标为 `stale_or_unrecorded_recheck_layout` 并提示复核；不能引用旧 manifest 宣称新文字已通过排版检查。改长文时优先同步 JSON 并重新 build；手工特殊布局则重新测量和看图。

只重新渲染：

```sh
node /absolute/path/to/handdrawn-infographics/scripts/render.cjs \
  /absolute/path/to/交付/manifest.json
```

缺字体、依赖或溢出时解决原因，不以转曲、假字、小字或截图代替 SVG。浏览器可直接预览内嵌字形；换机器在桌面编辑器里新增文字时安装输出 `fonts/` 中的完整字体。手工新增字不一定在旧的内嵌子集中，优先改 JSON 重建以更新子集。PNG 不依赖收件人的字体。

结构或风格代码修改后运行 `python3 scripts/test_style.py`：检查九种结构的正文图标、显式图标输入、树形连接笔触，以及手机集合图的图标与字号。此检查不代替全图和阅读尺度的视觉验收。
