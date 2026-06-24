# Day 18：sessions 查询接口练习指南

今天目标：

实现会话列表和会话消息查询接口。

## 任务要求

- 实现 GET `/sessions`。
- 实现 GET `/sessions/{session_id}/messages`。
- 找不到 session 时返回清晰错误。
- 在 Swagger 中测试。

## 先自己做

先用假数据实现接口，再接真实 storage。

## 一级提示

你需要思考：

```text
列表接口返回什么？
详情接口返回什么？
不存在时返回什么？
```

## 二级提示

错误处理可能会用到：

```python
from fastapi import HTTPException
```

## 自检清单

- `/sessions` 是否返回列表？
- `/sessions/{id}/messages` 是否返回消息？
- 不存在 id 是否返回 404？
- Swagger 是否至少测了 3 个场景？

## 完成标准

- 两个接口可用。
- 至少 3 个测试用例。
- 错误响应清楚。

