# 第1阶段：LLM API 与 FastAPI AI Chat

建议时间：第 1 个月，4 周

阶段目标：

- 掌握大模型 Chat API 调用。
- 掌握 messages、system prompt、temperature、streaming。
- 掌握结构化输出和异常处理。
- 完成一个 AI Chat 后端。

阶段项目：

```text
ai_chat_backend/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── chat.py
│   │   └── sessions.py
│   ├── services/
│   │   ├── llm_service.py
│   │   └── chat_service.py
│   └── storage/
│       └── json_storage.py
├── data/
├── .env
└── requirements.txt
```

## 第1周：LLM API 调用

目标：

- 能用 Python 独立调用一次大模型 API。
- 能实现命令行多轮对话。

每日计划：

- Day 1：创建项目、`.venv`、`.env`、安装 `httpx`、`python-dotenv`。
- Day 2：写 `chat_once.py`，完成一次问答。
- Day 3：写 `chat_loop.py`，用 list 保存多轮 messages。
- Day 4：加入 system prompt、temperature、max_tokens。
- Day 5：整理 README，记录请求体、响应体、5 个常见错误。

量化验收：

- 命令行连续对话不少于 5 轮。
- messages 中包含 system、user、assistant。
- API Key 不写死在代码里。
- README 包含运行命令。

## 第2周：Prompt 与结构化输出

目标：

- 能让模型按指定格式返回。
- 能处理 JSON 输出不稳定问题。

每日计划：

- Day 1：写 5 个 system prompt 模板。
- Day 2：写 few-shot 示例，让模型固定风格回答。
- Day 3：要求模型返回 JSON，完成 `json.loads()` 解析。
- Day 4：加入 JSON 解析异常处理和错误提示。
- Day 5：整理 Prompt 模板库和测试样例。

量化验收：

- 至少 5 个 prompt 模板。
- 至少 3 个结构化输出任务。
- 至少 10 个 prompt 测试输入。
- JSON 解析失败时程序不崩溃。

## 第3周：FastAPI Chat 接口

目标：

- 把 LLM 调用封装成 HTTP 接口。

每日计划：

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

## 第4周：会话历史与工程化

目标：

- 完成一个可作为作品的 AI Chat 后端。

每日计划：

- Day 1：设计 session_id、messages 数据结构。
- Day 2：保存会话历史到 JSON 或 SQLite。
- Day 3：实现 `/sessions` 和 `/sessions/{id}/messages`。
- Day 4：加入 streaming 或 WebSocket 二选一。
- Day 5：整理 README、接口文档、项目结构说明。

量化验收：

- 支持多会话。
- 支持查询历史消息。
- 服务重启后历史不丢。
- README 包含启动方式、接口列表、测试示例。

阶段完成标准：

- 能独立调用 LLM API。
- 能设计 messages 和 prompt。
- 能用 FastAPI 暴露 AI Chat 服务。
- AI Chat 后端项目可运行、可测试、可展示。

