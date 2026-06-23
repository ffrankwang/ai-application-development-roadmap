# Week 05：文档解析和切片

目标：

- 把文档转成可检索 chunks。

每日任务：

- Day 1：整理 RAG 流程：load、split、embed、search、generate。
- Day 2：实现 Markdown 文档读取。
- Day 3：实现固定长度文本切片。
- Day 4：给 chunk 增加 metadata：source、chunk_index、title。
- Day 5：保存 chunks 到 JSON，整理切片测试记录。

量化验收：

- 至少处理 5 个 Markdown 文档。
- 至少生成 100 个 chunk。
- 每个 chunk 包含 text、source、chunk_index。
- 能解释 chunk_size 和 overlap 的作用。

输出位置：

- 代码：`src/`
- 笔记：`notes/`

