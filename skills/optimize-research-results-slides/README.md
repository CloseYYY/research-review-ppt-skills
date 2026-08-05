# Optimize Research Results Slides

面向生命科学研究生与科研人员的中文实验结果型组会 PPT 优化 Skill。它可以整理已有 PPTX，也可以从实验记录、结果图片和提纲构建新的汇报，并把实验目的、关键方法与条件、直接结果、一句话结论和下一步实验组织成适合向导师汇报的清晰证据链。

## 适用场景

- 个人实验结果或阶段性研究进展组会
- 已有结果页结构松散、方法条件缺失或结论超出证据
- 从实验记录、图片、表格和简要提纲新建组会 PPTX
- 需要为隐藏图片、基因名、数值或结论保留可替换位置
- 需要逐页中文讲稿、术语全称和未来实验计划

本 Skill 专门处理以用户未公开实验数据为核心的结果型汇报。对于主要综合已发表文献、机制或方法的综述型组会，请使用 [`optimize-research-review-slides`](https://github.com/Guan-Bio/research-review-ppt-skills/tree/main/skills/optimize-research-review-slides)。

## 核心能力

- 同时支持优化已有 PPTX 和从原始材料新建 PPTX
- 将每张结果页整理为实验目的、实验方法与关键条件、实验结果、一句话结论
- 区分直接观察、相关性、功能支持和因果证据，保留阴性结果与不确定性
- 一次性发送按页汇总的缺失信息 Checklist，避免反复追问
- 接受“无 / 不适用 / 不清楚 / 已隐藏”，并转换为规范留白或占位
- 为隐藏图片、名称、数值和结论保留克制、可编辑的替换区域
- 为每组结果提出紧邻证据的下一步实验，并在末尾形成 P0–P2 优先级路线图
- 使用白色背景、统一无衬线字体、临床蓝强调色和 1.2–1.5 行距
- 为每页生成适合向导师汇报的中文讲稿并写入备注
- 在专业术语首次出现时补充中文名称、英文全称和缩写
- 审计备注、结果页必需字段、字体、背景、占位符、外部关系与演讲时长

## 保密原则

所有用户提供的实验结果、图片、结论、基因或靶点名称、代称映射、样本信息、文件名和备注均默认视为未公开信息。

- 机密材料只使用本地工作区工具处理。
- 不将用户实验内容或可识别的衍生信息发送到网页搜索、图像生成、外部 API 或无关任务。
- 不使用未公开图片进行反向图片搜索，也不要求外部模型解释实验数据。
- 不推测或还原被隐藏的基因名、结论、数值和图片内容。
- 公共背景检索只能使用无法识别用户研究的通用公开主题。
- 用户实验页在备注中标记为“用户提供的未公开数据”。
- 默认保留源文件并输出新的 PPTX，不覆盖原文件。

完整规范见 [`references/confidentiality.md`](references/confidentiality.md)。

## 依赖

- 使用 Codex 的 `presentations:Presentations` Skill 完成 PPTX 读取、编辑、渲染与导出。
- 背景知识页必须安装并调用 `optimize-research-review-slides`。
- 中文文本优先调用 `Humanizer Zh`；未安装时自动使用本 Skill 内置的中文科研表达规范。

## 安装

将整个仓库复制到 Codex 个人 Skills 目录，并保持目录名不变：

```text
Windows: %USERPROFILE%\.codex\skills\optimize-research-results-slides
macOS/Linux: ~/.codex/skills/optimize-research-results-slides
```

也可以克隆仓库：

```bash
git clone https://github.com/Guan-Bio/optimize-research-results-slides.git
```

安装后开启一个新任务，再上传 PPTX 或实验材料。

## 使用示例

优化已有结果型组会 PPT：

```text
请使用 $optimize-research-results-slides 优化这份实验结果型组会 PPT。
汇报对象是导师和课题组成员，主汇报 15 分钟。
请严格保密，不要把任何实验内容发送到外部服务。
缺失信息请一次性汇总成 Checklist；图片或基因名已隐藏的地方请保留占位。
```

从材料新建 PPT：

```text
请使用 $optimize-research-results-slides，根据这些实验记录、图片和统计结果创建中文组会 PPTX。
每张结果页需要包含实验目的、关键实验条件、实验结果和一句话结论，
并为每组结果提出下一步实验，最后汇总为按优先级排列的实验计划。
```

## 工作流程

1. 在本地审计输入并识别封面、背景、研究问题、结果、总结、未来计划和备用页。
2. 为每个结果单元建立目的、模型、设计、条件、读数、重复、统计、结果、结论边界与下一步记录。
3. 一次性发送缺失信息 Checklist，并等待用户集中回复。
4. 按证据重构结果页和讲稿，保留隐藏信息占位与解释边界。
5. 调用综述型 Skill 优化背景知识页。
6. 生成模块级下一步建议和总体实验路线图。
7. 渲染每一页，执行溢出检查和严格 PPTX 审计后交付。

## 审计脚本

审计器仅依赖 Python 标准库：

```bash
python scripts/audit_pptx.py FINAL.pptx --strict --require-white-background
```

可选参数：

```text
--required-font "Microsoft YaHei"
--require-line-spacing
--strict-terms
--target-minutes 15
--target-main-slides 14
--json
```

审计范围包括逐页备注标记、结果页四项必需信息、允许与意外占位、显式背景色、可见字体、行距、术语展开提示、外部关系、嵌入文件、评论和预计讲稿时长。

## 仓库结构

```text
optimize-research-results-slides/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── confidentiality.md
│   ├── domain-extensions.md
│   ├── intake-checklist.md
│   ├── quality-checklist.md
│   ├── results-deck-workflow.md
│   └── scientific-language.md
└── scripts/
    └── audit_pptx.py
```
