# Day 19：Streaming 或 WebSocket 练习指南

今天目标：

在 AI Chat 后端中加入流式体验，Streaming 或 WebSocket 二选一。

## 任务要求

二选一：

- 方案 A：HTTP streaming。
- 方案 B：WebSocket。

学习阶段建议优先选 HTTP streaming。

## 先自己做

先用模拟数据流：

```text
一段
一段
一段
地返回文本
```

模拟版跑通后，再接真实模型 streaming。

## 一级提示

你需要理解：

```text
普通响应：一次性返回完整结果
流式响应：边生成边返回
```

## 二级提示

FastAPI 中可能会用到：

```text
StreamingResponse
```

WebSocket 可能会用到：

```text
@app.websocket
```

## 自检清单

- 是否先跑通模拟流式？
- 客户端是否能看到分段输出？
- 出错时连接是否能结束？
- README 是否说明你选择了哪个方案？

## 完成标准

- Streaming 或 WebSocket 至少一个可运行。
- 有模拟测试。
- 有实现说明。

