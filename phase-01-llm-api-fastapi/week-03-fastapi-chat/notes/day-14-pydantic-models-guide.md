# Day 14：Pydantic 请求响应模型练习指南

今天目标：

用 Pydantic 定义清晰的请求和响应结构。

## 任务要求

- 新建或整理 `schemas.py`。
- 定义 `ChatRequest`。
- 定义 `ChatResponse`。
- 给字段增加基本校验。
- 让 Swagger 文档更清楚。

## 先自己做

思考接口需要哪些字段：

```text
message
session_id
reply
model
```

先不要一次设计太复杂。

## 一级提示

你会用到：

```python
from pydantic import BaseModel, Field
```

## 二级提示

可以限制：

```text
message 不能为空
message 最大长度
```

## 自检清单

- 每个 POST 接口是否有请求模型？
- 响应是否有明确结构？
- Swagger 是否展示字段说明？
- 错误输入是否能返回 422？

## 完成标准

- 至少 2 个 request/response schema。
- `/chat` 使用 schema。
- Swagger 字段清楚。

