# Day 4：system prompt 与参数练习指南

今天目标：

在多轮对话中加入 system prompt，并练习 `temperature`、`max_tokens` 等参数对回答的影响。

## 任务要求

- 在 messages 或 instructions 中加入系统角色。
- 支持从 `.env` 读取模型名。
- 设置并修改 `temperature`。
- 设置并修改 `max_tokens`。
- 记录不同参数下的回答差异。

## 先自己做

准备 3 个 system prompt：

- Python 学习导师。
- Java 后端转 AI 应用导师。
- 严格 JSON 输出助手。

同一个问题分别测试这 3 个 prompt。

## 一级提示

你需要观察：

```text
同一个 input
不同 instructions
不同 temperature
```

## 二级提示

建议测试问题：

```text
我已经会 Java 后端，应该如何学习 FastAPI？
```

参数建议：

```text
temperature = 0.2
temperature = 0.7
temperature = 1.0
```

## 自检清单

- 是否能修改 system prompt？
- 是否能修改 temperature？
- 是否能看出回答稳定性变化？
- 是否记录了测试结果？

## 笔记要求

在 `notes/` 下记录：

```text
prompt:
temperature:
question:
answer summary:
observation:
```

## 完成标准

- 至少测试 3 个 system prompt。
- 至少测试 3 个 temperature。
- 写出 5 条观察结论。

