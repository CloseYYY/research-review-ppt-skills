# Research Review PPT Skills

面向生命科学研究生和科研人员的中文综述型组会 PPT 优化技能。它以“草稿 PPT + 格式模板 PPT”为主要输入，帮助 Agent 完成内容补充、结构重组、版式统一、科学语言润色、图像与文献证据补充、逐页讲稿生成，以及汇报时长控制。

## 适用场景

- 文献综述、方法综述、专题综述和开题前的领域梳理
- 已有草稿内容较散，需要整理成可以正式汇报的 PPT
- 希望沿用实验室、课题组或答辩模板的视觉风格
- 需要“主汇报 + 备用页”结构，并按指定时长或页数压缩内容

本技能专门针对综述型汇报。对于以个人实验数据、结果链条和研究结论为核心的结果型组会，应采用另一套叙事和证据组织方式。

## 核心能力

- 优化前询问汇报时长或页数；用户也可以授权 Agent 自动判断
- 按“问题—证据—方法—应用—局限—建议”组织综述内容
- 支持主汇报页与备用页分离，给出建议讲述时间
- 参考模板统一白色背景、字体、字号、色彩、页眉页脚和图文比例
- 没有参考模板时提供 4 套内置白底配色：A 临床蓝（默认推荐）、B 生命青绿、C 编辑珊瑚、D 石墨靛蓝
- 将标题改写为自然、准确的生物学报告语言
- 使用严谨但易读的中文科学表达，并减少模板化、AI 化措辞
- 为应用案例补充已发表文献或可信在线资料中的图片和出处
- 为机制、通路、分子结构等内容生成或寻找简洁示意图
- 为每页生成讲稿并写入备注区
- 在术语首次出现的页面和讲稿中补充中文名称及英文全称
- 检查多行文字的行距、引用、图源、字体和汇报时长
- 提供免疫学、衰老、神经科学、肿瘤、代谢、微生物、植物、结构生物学、细胞生物学等生命科学方向的扩展规范

## 目录

```text
skills/
└── optimize-research-review-slides/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/audit_pptx.py
```

## Codex 安装

将 `skills/optimize-research-review-slides` 复制到个人 Codex 技能目录：

```text
Windows: %USERPROFILE%\.codex\skills\optimize-research-review-slides
macOS/Linux: ~/.codex/skills/optimize-research-review-slides
```

也可以在 Codex 中直接提出：

> 请从 GitHub 仓库 GuanBio/research-review-ppt-skills 安装 optimize-research-review-slides skill。

安装后开启一个新任务，再上传草稿 PPT 和格式模板 PPT。

## 使用示例

> 请用 optimize-research-review-slides 优化这份综述型组会 PPT。草稿是“错误折叠蛋白质检测方法汇总.pptx”，格式参考“博士论文答辩.pptx”。汇报 15 分钟，采用“主汇报 + 备用页”模式，中文，听众为生命科学研究生。请补充案例图、逐页讲稿、术语全称和参考文献。

如果没有格式模板，技能会询问默认配色。可以直接指定：

> 没有参考模板，请使用 A 临床蓝；如果我没有选择，采用推荐的 A。

如果不确定时长，可以写：

> 页数和汇报时长由你根据内容自动决定，并说明判断依据。

## TRAE WORK 与 WorkBuddy

本仓库采用通用的 `SKILL.md + references + scripts` 结构。若平台支持项目级 Skills，可将技能文件夹放入该平台约定的 skills 目录；若平台尚不能自动发现 Skills，可把 `SKILL.md` 作为主规则文件载入，并保持 `references/` 与 `scripts/` 的相对路径不变。不同版本的目录约定可能不同，安装后建议先用一份 3–5 页测试稿验证文件读取、PPT 编辑和备注写入能力。

## 发布与贡献

欢迎通过 Issue 提交生命科学子领域规范、审稿清单和真实汇报案例。提交案例时请移除未公开数据、受试者信息和无授权图片。

## License

[MIT License](LICENSE)
