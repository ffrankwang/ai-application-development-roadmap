# Day 9：JSON 解析异常处理练习指南

今天目标：

处理模型返回内容不是合法 JSON 的情况，让程序不崩溃。

## 任务要求

- 封装 `parse_json_response(text)`。
- 使用 `try/except` 捕获解析错误。
- 解析失败时返回错误信息。
- 记录原始模型输出。

## 先自己做

先手写一个坏 JSON：

```text
{"name": "Alice",
```

用它测试异常处理。

## 一级提示

你会用到：

```python
json.JSONDecodeError
```

## 二级提示

函数可以返回统一结构：

```python
{
    "success": False,
    "data": None,
    "error": "..."
}
```

## 自检清单

- 合法 JSON 是否能解析？
- 非法 JSON 是否不会崩溃？
- 是否保留了原始输出？
- 是否能给出清晰错误提示？

## 完成标准

- 至少测试 3 个合法 JSON。
- 至少测试 3 个非法 JSON。
- 程序不会因为解析失败退出。

