# Consolidated missing-information checklist

## Gate rule

Send one checklist after local audit, then wait for one consolidated reply. Do not ask the same missing field in separate messages. A response of `无`, `不适用`, `不清楚`, or `已隐藏` is complete.

Use this compact format:

```text
为避免替你猜测未公开结果，请一次性补充下表。可以直接填写“无 / 不适用 / 不清楚 / 已隐藏”。

全局
- 汇报时长或主汇报页数：
- 研究对象与听众需要知道的范围：
- 必须保留的代称、删减内容或保密限制：

第 N 页／结果单元：<当前可识别标题>
1. 实验目的：
2. 模型或样本：
3. 处理组、对照组及关键条件：
4. 检测方法与直接读数：
5. 生物学重复、技术重复及统计：
6. 直接实验结果：
7. 一句话结论及证据边界：
8. 已隐藏的图片、名称、数值或结论：
9. 已知限制与下一步考虑：
```

Include only fields genuinely missing from each unit. Retain slide numbers and titles so the user can respond unambiguously.

## Map responses

| User response | Visible slide treatment | Notes treatment |
|---|---|---|
| 无 / 不适用 | Omit when optional; otherwise leave the reserved field empty | State `用户确认本项无/不适用` only when omission could be misread |
| 不清楚 | Show `待确认：<field>` | State that interpretation is provisional because the field is unknown |
| 已隐藏 | Reserve a dashed placeholder labelled `待补：<type>` | State that the content was intentionally withheld |
| Alias | Preserve the alias verbatim | Do not infer or expand it |

Do not treat an unanswered field as `无`. If a reply omits a required field, keep it as `待确认` and state the limitation rather than starting another fragmented questionnaire.

## Placeholder sizing

- Experimental image or plot: reserve at least 45% of the slide canvas when it is the primary evidence.
- Secondary panel: reserve at least the size of adjacent panels and keep panel labels replaceable.
- Gene/protein/compound name: use `[待补：名称]` inline without changing grammar around the alias.
- Value: use `[待补：数值/单位]` and retain the unit only when known.
- Conclusion: use a full-width line labelled `[待补：一句话结论]`.

Use muted clinical blue or neutral gray borders, 1–1.5 pt dashed lines, no decorative icons, and no visual that could be mistaken for data.

