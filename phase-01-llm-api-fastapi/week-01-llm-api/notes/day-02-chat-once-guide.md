# Day 2：chat_once.py 一次问答练习指南

今天目标：

自己写出一个最小可运行脚本 `chat_once.py`，从命令行输入一个问题，调用大模型 API，并打印模型回答。

今天不是抄答案，而是练习把 API 调用链路自己搭起来。

核心链路：

```text
读取配置
  -> 接收用户输入
  -> 创建 API client
  -> 发送请求
  -> 读取回答
  -> 打印结果
```

## 今日交付物

你需要完成：

```text
week-01-llm-api/
├── src/
│   └── chat_once.py
└── notes/
    └── day-02-chat-once-guide.md
```

完成后，运行：

```bash
python chat_once.py
```

能够输入一个问题，并看到模型回答。

## 练习规则

先按下面顺序做：

1. 只看“任务要求”，自己写第一版。
2. 卡住 10 分钟后，看“一级提示”。
3. 继续卡住，再看“二级提示”。
4. 最后才看“参考答案”。

不要一开始看完整答案。

## 任务要求

请你自己实现 `chat_once.py`，满足这些要求：

- 从 `.env` 读取 API Key。
- 从 `.env` 读取模型名称。
- 使用 `input()` 接收用户问题。
- 调用大模型 API。
- 打印模型回答。
- API Key 不能写死在代码里。
- 程序入口使用 `if __name__ == "__main__":`。

## 环境准备

在仓库根目录激活虚拟环境：

```bash
cd C:\Users\wanghu\Desktop\AI应用开发\ai-application-development-roadmap
.\.venv\Scripts\Activate.ps1
```

安装依赖：

```bash
pip install openai python-dotenv
pip freeze > requirements.txt
```

在仓库根目录创建 `.env`：

```text
OPENAI_API_KEY=你的真实key
OPENAI_MODEL=你的模型名称
```

注意：

- `.env` 不要提交到 GitHub。
- 仓库已有 `.gitignore`，会忽略 `.env`。
- `.env.example` 只放示例，不放真实 key。

## 你可以查的关键词

如果忘了写法，可以查这些关键词，而不是直接看答案：

```text
python-dotenv load_dotenv
os.getenv
OpenAI Python SDK
client.responses.create
response.output_text
if __name__ == "__main__"
```

官方文档入口：

- OpenAI Developer Quickstart
- OpenAI Text generation guide
- OpenAI Python SDK

## 一级提示

你大概需要这些模块：

```python
import os
from dotenv import load_dotenv
from openai import OpenAI
```

你大概需要一个 `main()` 函数：

```python
def main():
    ...
```

你大概需要从环境变量读取模型名：

```python
model = os.getenv("OPENAI_MODEL")
```

## 二级提示

你的代码大概率会包含这些步骤：

```text
load_dotenv()
读取 OPENAI_MODEL
创建 OpenAI client
input() 获取用户问题
client.responses.create(...)
print(...) 输出回答
```

调用模型时，需要传入：

```text
model
instructions
input
```

其中：

- `model`：模型名称。
- `instructions`：给模型的角色和行为要求。
- `input`：用户这一次输入的问题。

## 自检清单

写完后检查：

- 是否导入了 `load_dotenv`？
- 是否调用了 `load_dotenv()`？
- 是否从环境变量读取了 `OPENAI_MODEL`？
- 是否没有把 API Key 写进代码？
- 是否用了 `input()`？
- 是否调用了模型 API？
- 是否打印了回答文本？
- 是否有 `if __name__ == "__main__":`？

## 运行方式

进入脚本目录：

```bash
cd C:\Users\wanghu\Desktop\AI应用开发\ai-application-development-roadmap\phase-01-llm-api-fastapi\week-01-llm-api\src
python chat_once.py
```

测试输入：

```text
什么是 FastAPI？
```

预期：

```text
AI: ...
```

能看到模型回答，就算 Day 2 主任务完成。

## 改写练习

主任务完成后，再做 3 个改写。

### 改写 1：固定问题

不用 `input()`，直接把问题写在变量里。

要求：

- 变量名叫 `user_question`。
- 问题内容是：`用三句话解释什么是大模型 API`。

### 改写 2：改变模型角色

修改 `instructions`。

要求：

- 让模型扮演“Java 后端工程师转 AI 应用开发的导师”。
- 观察回答风格是否变化。

### 改写 3：观察完整返回

打印完整 response。

要求：

- 除了最终文本，还要观察完整返回对象。
- 在笔记里记录你看到了哪些字段。

## 完成标准

今天完成后，你应该能做到：

- 能运行 `python chat_once.py`。
- 能输入一个问题并看到模型回答。
- 能说明 API Key 为什么不写在代码里。
- 能说明 `instructions` 和 `input` 的区别。
- 能把模型名改成从 `.env` 读取。

## 常见错误

### 1. 没有设置 API Key

现象：

```text
OPENAI_API_KEY is not set
```

处理：

- 检查 `.env` 是否在仓库根目录。
- 检查变量名是否是 `OPENAI_API_KEY`。
- 检查终端是否从正确目录运行。

### 2. 没有安装依赖

现象：

```text
ModuleNotFoundError: No module named 'openai'
```

处理：

```bash
pip install openai
```

### 3. 没有激活虚拟环境

现象：

- VS Code 能看到包，但终端运行报错。
- 或终端能运行，但 VS Code 报错。

处理：

- VS Code 选择 `.venv` 解释器。
- 终端激活 `.venv`。

------------------------------------------------------------------------

# 参考答案

先自己写。卡住 20 分钟以上，再看这里。

```python
import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()

    model = os.getenv("OPENAI_MODEL")
    if not model:
        raise ValueError("OPENAI_MODEL is not set")

    client = OpenAI()

    user_question = input("You: ")

    response = client.responses.create(
        model=model,
        instructions="你是一个简洁、准确的 AI 应用开发学习助手。",
        input=user_question
    )

    print("AI:", response.output_text)


if __name__ == "__main__":
    main()
```

看完参考答案后，不要直接复制。

正确做法：

1. 关掉答案。
2. 自己重新写一遍。
3. 运行。
4. 报错后自己根据报错修改。

