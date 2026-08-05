# Research PPT Skills

面向生命科学研究生和科研人员的中文科研 PPT Skills 集合。仓库目前包含综述型组会和实验结果型组会两套独立工作流，覆盖内容梳理、证据边界、科学语言、版式统一、逐页讲稿、术语全称、时长控制和渲染质检。

## 选择合适的 Skill

| Skill | 适用汇报 | 核心任务 |
|---|---|---|
| [`optimize-research-review-slides`](skills/optimize-research-review-slides/) | 文献综述、方法综述、专题梳理、机制或领域进展 | 按公开文献组织问题、证据、方法、局限与建议，并补充可追溯图源 |
| [`optimize-research-results-slides`](skills/optimize-research-results-slides/) | 个人实验结果、阶段进展、数据复盘、未来实验计划 | 整理实验目的、方法与关键条件、结果、一句话结论和下一步验证，并严格保护未公开数据 |

如果 PPT 同时包含两类内容，以主要证据来源决定主 Skill：个人未公开实验数据为主时使用结果型 Skill，背景知识页再调用综述型 Skill；已发表知识综合为主时使用综述型 Skill。

## 共同能力

- 中文生命科学组会语境，面向导师和课题组成员
- 白色背景、统一无衬线字体和清晰图文层级
- 严谨、科学、清楚的中文表达，减少模板化和 AI 化措辞
- 多行内容使用 1.2–1.5 行距
- 为每页生成讲稿并写入备注区
- 在非常见术语首次出现时补充中文名称、英文全称和缩写
- 控制主汇报时长或页数，并支持备用页
- 渲染每一页，检查文本溢出、重叠、字体、备注和来源
- 输出可继续编辑的 PPTX

## 两个工作流的关键区别

### 综述型组会

- 主要处理已发表文献、方法、机制和领域比较。
- 可检索公开文献与权威数据库，补充公开案例图和来源。
- 按“问题—证据—方法—应用—局限—建议”组织叙事。
- 不作为用户新实验结果的主工作流。

### 结果型组会

- 主要处理用户未公开实验数据、阶段结论和后续实验。
- 每张结果页必须清楚呈现实验目的、实验方法与关键条件、实验结果和一句话结论。
- 缺失信息先通过一次性 Checklist 集中补充；支持“无 / 不适用 / 不清楚 / 已隐藏”。
- 不把实验内容或可识别衍生信息发送到网页搜索、图像生成、外部 API 或无关任务。
- 为每组结果提出下一步实验，并形成按优先级排列的总体路线图。

## 安装

将需要的 Skill 文件夹复制到个人 Codex Skills 目录：

```text
Windows: %USERPROFILE%\.codex\skills\<skill-name>
macOS/Linux: ~/.codex/skills/<skill-name>
```

例如安装两套 Skill：

```text
~/.codex/skills/optimize-research-review-slides/
~/.codex/skills/optimize-research-results-slides/
```

也可以先克隆仓库：

```bash
git clone https://github.com/Guan-Bio/research-ppt-skills.git
```

每个 Skill 必须保持自身的 `SKILL.md`、`agents/`、`references/`、`scripts/` 和 `assets/` 相对路径不变。

## 使用示例

综述型汇报：

```text
请使用 $optimize-research-review-slides 优化这份生命科学综述型组会 PPT。
主汇报 15 分钟，中文，背景为白色；请补充公开案例图、逐页讲稿、术语全称和参考文献。
```

结果型汇报：

```text
请使用 $optimize-research-results-slides 优化这份实验结果型组会 PPT。
请严格保密；每张结果页包含实验目的、关键实验条件、实验结果和一句话结论。
缺失信息请一次性汇总为 Checklist，最后给出按优先级排列的后续实验计划。
```

## 仓库结构

```text
research-ppt-skills/
├── README.md
├── LICENSE
└── skills/
    ├── optimize-research-review-slides/
    │   ├── SKILL.md
    │   ├── agents/
    │   ├── assets/
    │   ├── references/
    │   └── scripts/
    └── optimize-research-results-slides/
        ├── README.md
        ├── SKILL.md
        ├── agents/
        ├── references/
        └── scripts/
```

## 平台兼容

仓库使用通用的 `SKILL.md + references + scripts + assets` 结构。不同平台的 PPTX 编辑能力可能不同，但应保持以下验收要求：保留源文件、生成新 PPTX、写入逐页备注、保留来源、渲染并逐页检查最终成品。

## 贡献与保密

欢迎通过 Issue 或 Pull Request 提交生命科学子领域规则、审稿清单和合成测试案例。请勿上传未公开实验数据、受试者信息、真实样本标识、代称映射或无授权图片。

## License

[MIT License](LICENSE)
