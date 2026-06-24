# Day 17：会话历史持久化练习指南

今天目标：

把聊天历史保存到 JSON 或 SQLite，服务重启后不丢数据。

## 任务要求

- 选择 JSON 或 SQLite。
- 实现保存会话。
- 实现读取会话。
- 重启服务后还能查到历史。

## 先自己做

如果不确定选哪个，先选 JSON。

练习重点不是数据库，而是：

```text
业务对象
  -> 持久化格式
  -> 再读回来
```

## 一级提示

JSON 方案会用到：

```python
json.dump
json.load
os.path.exists
```

## 二级提示

建议封装：

```text
load_sessions()
save_sessions(sessions)
```

## 自检清单

- 文件不存在时是否返回空列表或空 dict？
- 保存后文件是否可读？
- 重启服务后是否仍能加载？
- storage 逻辑是否和 router 分开？

## 完成标准

- 至少保存 2 个 session。
- 重启服务后能读回。
- storage 代码独立成文件。

