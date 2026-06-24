# Day 12：模拟版 /chat 接口练习指南

今天目标：

实现 POST `/chat`，先不接真实模型，只返回模拟回答。

## 任务要求

- 定义请求体：用户问题。
- 定义响应体：助手回答。
- 实现 POST `/chat`。
- 在 Swagger 中测试。

## 先自己做

不要直接调用模型。先让接口返回：

```text
你刚才说的是：xxx
```

## 一级提示

你会用到：

```python
from pydantic import BaseModel
```

## 二级提示

你需要两个模型：

```text
ChatRequest
ChatResponse
```

## 自检清单

- 请求字段是否是 `message`？
- 响应字段是否是 `reply`？
- Swagger 是否能测试？
- 空 message 是否暂时能发现？

## 完成标准

- `/chat` 可 POST。
- Swagger 至少测试 3 个问题。
- 不依赖 LLM API 也能跑通。

