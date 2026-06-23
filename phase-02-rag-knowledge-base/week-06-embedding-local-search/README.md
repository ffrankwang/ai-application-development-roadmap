# Week 06：Embedding 与本地向量搜索

目标：

- 实现基于语义的 TopK 检索。

每日任务：

- Day 1：调用 embedding API，查看向量维度。
- Day 2：批量生成 chunk embeddings。
- Day 3：实现 cosine similarity。
- Day 4：输入问题，返回 Top 5 chunks。
- Day 5：用 10 个问题测试检索效果。

量化验收：

- 至少 100 个 chunk 有 embedding。
- 查询能返回 Top 5。
- 至少 10 个问题有测试记录。
- 检索结果包含 source 和相似度分数。

输出位置：

- 代码：`src/`
- 笔记：`notes/`

