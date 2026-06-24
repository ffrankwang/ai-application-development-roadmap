# Day 20：Phase 01 项目收尾与复盘指南

今天目标：

把 Phase 01 的 AI Chat 后端整理成一个可以展示、可以继续扩展的项目。

## 任务要求

- 整理项目 README。
- 整理接口文档。
- 整理运行命令。
- 整理测试用例。
- 清理无用文件。
- 确认 `.env` 未提交。

## README 必须包含

```text
项目简介
功能列表
技术栈
目录结构
环境变量
安装依赖
启动命令
接口列表
测试用例
下一步计划
```

## 自检清单

- 新电脑 clone 后能否按 README 跑起来？
- `/health` 是否可用？
- `/chat` 是否可用？
- `/sessions` 是否可用？
- 历史记录是否能保存？
- API Key 是否安全？

## 量化验收

- 至少 5 个接口测试用例。
- 至少 1 个完整演示流程。
- README 能指导别人启动。
- Phase 01 代码可以作为 GitHub 阶段成果。

## 复盘问题

- LLM API 和普通业务 API 最大差异是什么？
- Prompt、messages、history 分别解决什么问题？
- FastAPI 和 Spring Boot 的相似点与差异是什么？
- Phase 02 做 RAG 时，当前项目哪些代码可以复用？

