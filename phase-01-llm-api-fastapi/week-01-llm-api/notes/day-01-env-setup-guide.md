# Day 1：环境与配置练习指南

今天目标：

搭好 Phase 01 的 Python 开发环境，完成 `.venv`、依赖安装、`.env`、`.env.example` 和基础目录检查。

## 任务要求

- 在仓库根目录创建 `.venv`。
- VS Code 选择 `.venv` 解释器。
- 安装 `openai`、`python-dotenv`、`httpx`。
- 创建真实 `.env`。
- 确认 `.env` 不会提交到 GitHub。
- 更新 `requirements.txt`。

## 先自己做

不要看命令答案，先自己回忆并执行：

- 创建虚拟环境的命令。
- 激活虚拟环境的命令。
- 安装 pip 包的命令。
- 导出依赖的命令。

## 一级提示

你会用到这些关键词：

```text
python -m venv
Activate.ps1
pip install
pip freeze
requirements.txt
```

## 二级提示

检查点：

- 终端前面是否出现 `(.venv)`。
- `python --version` 是否正常。
- `pip list` 是否能看到依赖。
- `.gitignore` 是否包含 `.env` 和 `.venv/`。

## 自检清单

- `.venv` 在仓库根目录。
- `.env` 在仓库根目录。
- `.env.example` 没有真实 key。
- `requirements.txt` 已生成。
- VS Code 右下角解释器是 `.venv`。

## 完成标准

- 能激活虚拟环境。
- 能运行 `python --version`。
- 能运行 `pip show openai`。
- `git status` 不显示 `.env`。

## 参考命令

卡住 10 分钟后再看：

```bash
cd C:\Users\wanghu\Desktop\AI应用开发\ai-application-development-roadmap
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install openai python-dotenv httpx
pip freeze > requirements.txt
```

