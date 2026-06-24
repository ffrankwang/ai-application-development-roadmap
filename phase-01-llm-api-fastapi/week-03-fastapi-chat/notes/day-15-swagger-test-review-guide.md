# Day 15：Swagger 测试与 Week 03 复盘指南

今天目标：

用 Swagger 完成接口测试，并整理 FastAPI Chat 服务的阶段文档。

## 任务要求

- 测试 `/health`。
- 测试 `/chat`。
- 记录至少 5 个测试用例。
- 整理启动命令。
- 更新本周 README。

## 测试记录格式

```text
接口：
请求：
预期：
实际：
是否通过：
备注：
```

## 自检清单

- 服务能否从零启动？
- `.env` 缺失时错误是否清楚？
- `/chat` 是否真实调用模型？
- README 是否写了依赖安装和启动命令？

## 完成标准

- 至少 5 个 Swagger 测试用例。
- README 可指导别人启动。
- 能解释 router、schema、service 的分工。

