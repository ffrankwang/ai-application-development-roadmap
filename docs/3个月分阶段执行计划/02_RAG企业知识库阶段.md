# 第2阶段：RAG 企业知识库

建议时间：第 2 个月，4 周

阶段目标：

- 掌握 RAG 全链路。
- 完成文档解析、切片、Embedding、向量检索。
- 完成企业知识库问答服务。
- 回答中包含引用来源。

阶段项目：

```text
rag_knowledge_base/
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── documents.py
│   │   └── qa.py
│   ├── services/
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   ├── retrieval_service.py
│   │   └── qa_service.py
│   ├── loaders/
│   ├── splitters/
│   └── vector_store/
├── documents/
├── data/
└── requirements.txt
```

## 第1周：文档解析和切片

目标：

- 把文档转成可检索 chunks。

每日计划：

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

## 第2周：Embedding 与本地向量搜索

目标：

- 实现基于语义的 TopK 检索。

每日计划：

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

## 第3周：向量数据库

目标：

- 使用 PostgreSQL + pgvector 或 Milvus 持久化向量。

每日计划：

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

## 第4周：知识库问答服务

目标：

- 完成企业知识库助手基础版。

每日计划：

- Day 1：设计 `/documents/upload` 和 `/ask` 接口。
- Day 2：实现文档入库流程。
- Day 3：实现检索增强 prompt。
- Day 4：回答中加入引用来源。
- Day 5：完成 README、接口文档、10 个演示问答。

量化验收：

- 支持文档入库。
- `/ask` 能基于知识库回答。
- 回答至少包含 1 条引用来源。
- 至少 10 个问答测试样例。

阶段完成标准：

- 能讲清楚 RAG 全链路。
- 能实现文档切片和向量检索。
- 能完成带引用来源的知识库问答。
- RAG 项目可运行、可测试、可展示。

