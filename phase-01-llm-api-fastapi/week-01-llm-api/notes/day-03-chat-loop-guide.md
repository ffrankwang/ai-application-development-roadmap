# Day 3：chat_loop.py 多轮对话练习指南

今天目标：

在 Day 2 的一次问答基础上，实现命令行多轮对话。

## 任务要求

- 新建 `src/chat_loop.py`。
- 使用 `while True` 持续接收用户输入。
- 输入 `exit` 时退出。
- 用 list 保存 messages。
- 每轮都把 user 消息加入 messages。
- 每轮回答后，把 assistant 消息也加入 messages。

## 先自己做

先不要写 API 调用，先写一个模拟版：

```text
用户输入
  -> 加入 messages
  -> 打印模拟回答
  -> 把模拟回答加入 messages
```

模拟版跑通后，再接真实 API。

## 一级提示

你会用到：

```python
messages = []
while True:
    user_input = input("You: ")
```

退出判断：

```python
if user_input == "exit":
    break
```

## 二级提示

messages 的结构类似：

```python
{"role": "user", "content": "..."}
{"role": "assistant", "content": "..."}
```

每轮请求前，先 append user。

收到回答后，再 append assistant。

## 自检清单

- 是否支持多轮输入？
- 是否支持 `exit` 退出？
- messages 是否越来越长？
- user 和 assistant 是否成对出现？
- 是否没有把 API Key 写死？

## 改写练习

- 输入空字符串时提示重新输入。
- 输入 `history` 时打印当前 messages。
- 限制最多保留最近 5 轮对话。

## 完成标准

- 能连续对话不少于 5 轮。
- 能打印完整历史。
- messages 中包含 user 和 assistant。

## 参考结构

卡住后再看：

```python
messages = [
    {"role": "system", "content": "你是一个简洁的助手。"}
]

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    messages.append({"role": "user", "content": user_input})
    # call model here
    messages.append({"role": "assistant", "content": "..."})
```

