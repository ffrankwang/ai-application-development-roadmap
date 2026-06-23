# Week 07：向量数据库

目标：

- 使用 PostgreSQL + pgvector 或 Milvus 持久化向量。

每日任务：

- Day 1：搭建向量数据库环境。
- Day 2：设计 documents、chunks 表结构。
- Day 3：写入 documents、chunks、embeddings。
- Day 4：实现数据库 TopK 检索。
- Day 5：封装 FastAPI `/search` 接口。

量化验收：

- 数据库中至少保存 100 个 chunks。
- `/search` 可返回 TopK 检索结果。
- 检索结果包含 source、chunk_text、score。
- README 包含数据库启动和初始化说明。

输出位置：

- 代码：`src/`
- 笔记：`notes/`

