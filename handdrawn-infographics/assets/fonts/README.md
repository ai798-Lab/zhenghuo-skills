# 小赖手写字体

默认采用 Xiaolai Regular（小赖），与用户确认的手写样张一致。完整原始 TTF 用于文字测量、PNG 导出及继续编辑；SVG 另嵌入当前图中文字的 WOFF2 子集，全部文字仍为可编辑 `<text>`。

- 作者项目：https://github.com/lxgw/kose-font
- 固定版本：v3.126；为保持已确认字形，未自动追随上游新版本。
- 原始文件：https://github.com/lxgw/kose-font/releases/download/v3.126/Xiaolai-Regular.ttf
- SHA-256：`e2f68daf0e72777a8cf58bc83de1b98634b251e537ddbfca24b0ae50d1802da2`
- 许可：SIL Open Font License 1.1，完整原文见同目录 `OFL.txt`。

## 商用和分发

按作者的[官方授权说明](https://github.com/lxgw/kose-font#授权信息)，个人、企业均可免费商用，无需另行知会作者。可用于图书、文章、课程、广告及商业设计；使用该字体制作的图文作品不因此必须采用 OFL 许可。

本 Skill 连同字体文件分发，保留版权声明和完整 OFL 许可证。不要将字体文件单独出售；修改或衍生字体仍需遵守 OFL，不能将字体本身改成 MIT 许可。

## 编辑文字

浏览器可直接显示 SVG 中嵌入的当前用字。若在桌面编辑器中新增或修改文字，先安装完整 `Xiaolai-Regular.ttf`，再选择字体 `Xiaolai`；编辑器对内嵌字体的支持各不相同。优先修改 JSON 后重新生成，可同时更新字形子集、换行和 PNG。

Xiaolai 只有一个真实字重，标题与正文均使用 400，通过字号、高亮与留白区分层级，不使用伪粗体或随机扭曲字形。生成脚本直接从包内读取字体，无需事先安装到操作系统。
