# Day 11：FastAPI /health 接口练习指南

今天目标：

创建最小 FastAPI 项目，并实现 `/health` 接口。

## 任务要求

- 安装 `fastapi` 和 `uvicorn`。
- 新建 FastAPI app。
- 实现 GET `/health`。
- 启动服务。
- 打开 `/docs`。

## 先自己做

先不要接 LLM，只做最小 Web 服务。

## 一级提示

你会用到：

```python
from fastapi import FastAPI
```

## 二级提示

接口返回：

```json
{"status": "ok"}
```

启动命令关键词：

```text
uvicorn
--reload
```

## 自检清单

- `/health` 是否返回 200？
- `/docs` 是否能打开？
- 代码是否放在 `src/` 里？
- README 是否记录启动命令？

## 完成标准

- 服务可启动。
- `/health` 可访问。
- `/docs` 可访问。

