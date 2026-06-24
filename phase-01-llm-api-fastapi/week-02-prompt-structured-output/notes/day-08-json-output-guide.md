# Day 8：JSON 结构化输出练习指南

今天目标：

让模型返回 JSON，并用 Python 解析结果。

## 任务要求

- 设计一个 JSON 输出 schema。
- 要求模型只返回 JSON。
- 用 `json.loads()` 解析。
- 打印解析后的字段。

## 推荐任务

让模型分析一段 SQL，返回：

```text
summary
risk_level
problems
suggestions
```

## 一级提示

你需要：

```python
import json
```

解析：

```python
data = json.loads(text)
```

## 二级提示

prompt 中要明确：

```text
只返回 JSON
不要 Markdown
不要代码块
不要额外解释
```

## 自检清单

- 是否真的拿到了 JSON 字符串？
- 是否能 `json.loads()`？
- 是否打印了指定字段？
- 如果模型返回 Markdown 代码块，是否能发现问题？

## 完成标准

- 至少 3 个 JSON 输出任务。
- 至少 1 次解析成功。
- 记录 3 种可能失败的返回格式。

