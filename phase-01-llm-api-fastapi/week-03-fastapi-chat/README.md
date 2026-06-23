# Week 03：FastAPI Chat 接口

目标：

- 把 LLM 调用封装成 HTTP 接口。

每日任务：

- Day 1：创建 FastAPI 项目，写 `/health`。
- Day 2：写 `/chat`，先返回模拟回答。
- Day 3：接入真实 LLM API。
- Day 4：使用 Pydantic 定义 `ChatRequest`、`ChatResponse`。
- Day 5：用 Swagger 完成接口测试并整理文档。

量化验收：

- `uvicorn app.main:app --reload` 可启动。
- `/docs` 可访问。
- `/chat` 能返回真实模型回答。
- 至少 5 个 Swagger 测试用例。

输出位置：

- 代码：`src/`
- 笔记：`notes/`

