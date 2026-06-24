# Day 13：接入真实 LLM API 练习指南

今天目标：

把模拟版 `/chat` 改成真实调用 LLM API。

## 任务要求

- 封装 `llm_service`。
- `/chat` 调用 service，而不是直接写 API 细节。
- 从 `.env` 读取模型名和 API Key。
- 返回真实模型回答。

## 先自己做

先设计分层：

```text
router
  -> chat_service
  -> llm_service
  -> OpenAI API
```

## 一级提示

不要把 API 调用写在 router 里。

router 只负责：

```text
接收请求
调用 service
返回响应
```

## 二级提示

`llm_service` 里可以有一个函数：

```text
generate_reply(message)
```

## 自检清单

- API Key 是否仍然不在代码里？
- router 是否足够薄？
- 出错时是否能看出是 LLM 调用失败？
- Swagger 是否能拿到真实回答？

## 完成标准

- `/chat` 返回真实模型回答。
- 至少 5 个 Swagger 测试通过。
- 代码已拆分 service。

