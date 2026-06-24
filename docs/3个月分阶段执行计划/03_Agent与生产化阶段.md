# 第3阶段：Agent 与生产化

建议时间：第 3 个月，4 周

阶段目标：

- 掌握 Function Calling / Tool Calling。
- 完成 AI SQL/日志分析助手。
- 掌握轻量 Agent 工作流。
- 把项目 Docker 化，整理成可展示作品。

阶段项目：

```text
ai_dev_assistant/
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── routers/
│   ├── agents/
│   ├── tools/
│   ├── workflows/
│   └── services/
├── examples/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 第1周：Function Calling / Tool Calling

目标：

- 让模型根据问题选择并调用工具。

每日计划：

- Day 1：理解 tool schema，定义工具输入输出。
- Day 2：实现 `calculate` 工具。
- Day 3：实现 `get_current_time` 工具。
- Day 4：实现 `search_knowledge_base` 工具。
- Day 5：整理工具调用日志和 10 个测试问题。

量化验收：

- 至少 3 个工具。
- 至少 10 个测试问题。
- 能打印工具名、参数、返回值。
- 模型能根据问题选择合适工具。

## 第2周：AI SQL/日志分析助手

目标：

- 做一个贴近 Java 后端工作的 AI 开发助手。

每日计划：

- Day 1：准备 10 条 SQL 样例，定义输出结构。
- Day 2：实现 SQL 解释和优化建议。
- Day 3：准备 10 条错误日志样例。
- Day 4：实现日志原因分析和排查步骤。
- Day 5：封装 `/analyze-sql` 和 `/analyze-log` 接口。

量化验收：

- `/analyze-sql` 可用。
- `/analyze-log` 可用。
- 每个接口至少 10 个测试样例。
- 输出包含问题说明、原因分析、优化或排查建议。

## 第3周：轻量 Agent 工作流

目标：

- 用工作流组织多步骤 AI 任务。

每日计划：

- Day 1：理解 state、node、edge。
- Day 2：实现 SQL 分析工作流：解析、诊断、建议。
- Day 3：实现日志分析工作流：提取、归因、排查。
- Day 4：加入工具调用节点或重试节点。
- Day 5：整理工作流图和 README。

量化验收：

- 至少 1 个可运行工作流。
- 工作流至少 3 个节点。
- 能打印每个节点的输入输出。
- 能展示从输入到最终结果的状态流转。

## 第4周：部署与作品整理

目标：

- 把项目整理成可展示、可部署的作品。

每日计划：

- Day 1：为 AI Chat 或 RAG 项目写 Dockerfile。
- Day 2：写 docker-compose.yml。
- Day 3：加入结构化日志和基础错误处理。
- Day 4：整理 README、架构图、接口文档。
- Day 5：完成最终演示和 3 个月复盘。

量化验收：

- `docker compose up` 可启动。
- `/health` 可访问。
- 至少 5 个接口测试通过。
- README 包含启动、接口、架构、测试样例。
- 至少 1 个项目可作为作品展示。

阶段完成标准：

- 能解释 Agent 和普通 Chat 的区别。
- 能让模型调用工具。
- 能完成 SQL/日志分析助手。
- 能把 AI 应用 Docker 化部署。
- 有一个完整可展示项目。

