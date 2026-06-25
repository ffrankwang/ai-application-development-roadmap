# Week 02：Prompt 与结构化输出

## 本周成果

- 5 个 system prompt 模板（历史、票据、医疗、SQL、Python）
- 2 个 few-shot prompt（历史问答 3 示例、SQL 优化 2 示例）
- 3 个 JSON 输出 schema（SQL 分析、代码审查、日志分析）
- JSON 解析异常处理：`parse_json_response()` 统一返回 `{success, data, error}`
- 15 个单元测试（7 合法 JSON + 8 非法 JSON），程序不会因解析失败崩溃

## 项目结构

```
week-02-prompt-structured-output/
├── src/
│   ├── prompt_templates.py        # 4 个 system prompt 模板 + 历史 few-shot
│   ├── sql_analyzer.py            # SQL 分析脚本（JSON 输出 + 异常处理）
│   └── test_system_prompts.py     # 交互式 prompt 测试脚本
├── tests/
│   ├── __init__.py
│   └── test_sql_analyzer.py       # parse_json_response 单元测试
├── notes/
│   ├── day-06-system-prompts-guide.md
│   ├── day-07-few-shot-guide.md
│   ├── day-08-json-output-guide.md
│   ├── day-09-json-error-handling-guide.md
│   ├── day-10-prompt-library-review-guide.md
│   └── day-10-prompt-library.md   # Prompt 模板库（本周整理成果）
└── README.md
```

## 运行说明

### 环境准备

```bash
pip install python-dotenv openai
```

在 `src/` 目录下创建 `.env` 文件：

```
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4o
```

### 运行脚本

```bash
# SQL 分析（JSON 结构化输出）
cd src && python sql_analyzer.py

# 历史问答（Few-shot 风格）
cd src && python test_system_prompts.py
```

### 运行测试

```bash
cd week-02-prompt-structured-output
python -m unittest discover tests -v
```

## Prompt 设计经验

1. **角色 + 任务 + 格式 + 限制 = 稳定输出**：四要素缺一不可
2. **Few-shot 覆盖面比数量重要**：3 个不同类型的示例比 10 个同类示例更有效
3. **JSON 输出必须兜底**：`try/except json.JSONDecodeError` 是必需的工程实践

## 量化验收

| 指标 | 目标 | 完成 |
|------|------|------|
| Prompt 模板 | ≥5 | 5 |
| 结构化输出任务 | ≥3 | 3 |
| 测试输入 | ≥10 | 15 |
| JSON 解析失败不崩溃 | ✓ | ✓ |
| Few-shot prompt | ≥1 | 2 |
| Prompt 设计经验 | ≥3 | 3 |
