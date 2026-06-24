# Day 16：session_id 与消息结构设计指南

今天目标：

为 AI Chat 后端设计多会话数据结构。

## 任务要求

- 设计 `session_id`。
- 设计 messages 结构。
- 区分 user 和 assistant。
- 支持一个用户多个会话。

## 先自己做

先画数据结构，不急着写代码。

你至少要设计：

```text
session
message
```

## 一级提示

一个 session 可以包含：

```text
id
title
created_at
updated_at
messages
```

## 二级提示

一个 message 可以包含：

```text
role
content
created_at
```

## 自检清单

- 能不能按 session_id 找到消息？
- 能不能列出所有 session？
- 能不能保存多轮历史？
- 是否考虑 created_at？

## 完成标准

- 写出数据结构样例。
- 至少准备 2 个 session 测试数据。
- 能说明为什么需要 session_id。

