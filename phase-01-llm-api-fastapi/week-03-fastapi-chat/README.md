# Week 03：FastAPI Chat 接口

## 功能

把 LLM 调用封装成 HTTP 接口，支持多轮对话。

## 目录结构

```
src/
├── main.py          # FastAPI 应用入口，定义 /health 和 /chat 路由
├── schemas.py       # Pydantic 请求响应模型（ChatRequest / ChatResponse）
├── llm_service.py   # 业务层：会话管理 + 调用 LLM API
└── .env.example     # 环境变量模板
```

路由、schema、service 的分工：
- **main.py（路由层）**：接收 HTTP 请求，参数校验，调用 service，返回响应
- **schemas.py（数据层）**：定义接口契约，字段校验 + Swagger 文档
- **llm_service.py（业务层）**：管理会话历史，封装 OpenAI SDK 调用，不感知 HTTP

## 环境准备

### 1. 安装依赖

```bash
pip install fastapi uvicorn python-dotenv openai
```

### 2. 配置环境变量

在项目根目录 `ai-application-development-roadmap/.env` 中配置：

```env
LLM_API_KEY=your-api-key
LLM_BASE_URL=https://api.deepseek.com
LLM_MODEL=deepseek-v4-pro
```

### 3. 启动服务

```bash
cd src
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### 4. 访问

- Swagger 文档：http://127.0.0.1:8000/docs
- 健康检查：http://127.0.0.1:8000/health

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/health` | 健康检查 |
| POST | `/chat` | 发送消息，返回 AI 回复 |

### POST /chat 请求示例

```json
{
  "message": "你好",
  "session_id": null,
  "model": null
}
```

- `session_id` 不传或为 null → 创建新会话
- `session_id` 传入已有 ID → 续接多轮对话
- `model` 不传则使用 `.env` 中的默认模型

## 测试记录

### 用例 1：健康检查

```
接口：GET /health
请求：无参数
预期：{"status": "ok"}
实际：{"status": "ok"}
通过：是
备注：验证服务正常运行
```

### 用例 2：发送消息（新会话）

```
接口：POST /chat
请求：{"message": "用一句话介绍深度学习"}
预期：返回 reply + 自动生成的 session_id
实际：{"reply": "深度学习是一种通过多层神经网络...", "session_id": "0491b857-...", "model": "deepseek-v4-pro"}
通过：是
备注：不传 session_id，服务端自动创建会话
```

### 用例 3：空消息校验

```
接口：POST /chat
请求：{"message": ""}
预期：返回 422，提示 message 不能为空
实际：422, {"detail": [{"type": "string_too_short", "msg": "String should have at least 1 character"}]}
通过：是
备注：Pydantic min_length=1 校验生效
```

### 用例 4：多轮对话——记住上文

```
接口：POST /chat
请求：{"message": "我刚才问的是什么问题？", "session_id": "0491b857-..."}
预期：AI 能回答出第一轮的问题
实际：{"reply": "你刚才问的是：'用一句话介绍深度学习'。"}
通过：是
备注：session_store 成功保留了对话历史
```

### 用例 5：多轮对话——深层引用

```
接口：POST /chat
请求：{"message": "重复一下我刚才的问题，用中文问回来", "session_id": "0491b857-..."}
预期：AI 能追溯前两轮的问题
实际：{"reply": "用一句话介绍深度学习"}
通过：是
备注：多轮上下文保持完整
```

### 用例 6：Swagger 文档可访问

```
接口：GET /docs
请求：浏览器访问
预期：返回 200，展示交互式 API 文档
实际：200 OK
通过：是
备注：FastAPI 自动生成的 OpenAPI 文档正常
```

## 量化验收

- `/docs` 可访问 ✓
- `/chat` 能返回真实模型回答 ✓
- `ChatRequest` / `ChatResponse` 至少 2 个 schema ✓
- 至少 5 个 Swagger 测试用例 ✓
- `.env` 缺失时启动报错清晰 ✓
