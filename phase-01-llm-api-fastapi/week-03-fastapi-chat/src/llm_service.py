import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 从当前文件向上查找到项目根目录的全局 .env
load_dotenv(Path(__file__).resolve().parent.parent.parent.parent / ".env")

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL = os.getenv("LLM_MODEL")

if not all([API_KEY, BASE_URL, MODEL]):
    print("错误：请确保 .env 文件中定义了 LLM_API_KEY, LLM_BASE_URL, LLM_MODEL")
    sys.exit(1)

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 会话存储：{ session_id: [ {"role": ..., "content": ...}, ... ] }
session_store: dict[str, list[dict]] = {}

SYSTEM_PROMPT = "百科全书工具，请根据用户输入给出答案。"


def get_extra_params(model: str):
    extra = {}
    if "reasoner" in model.lower():
        extra["reasoning_effort"] = "high"
        extra["extra_body"] = {"thinking": {"type": "enabled"}}
    return extra


def generate_reply(message: str, session_id: str) -> str | None:
    """多轮对话：根据 session_id 获取历史，拼入完整的 messages 后调用 LLM。"""
    # 首次会话：初始化 messages 列表
    if session_id not in session_store:
        session_store[session_id] = [{"role": "system", "content": SYSTEM_PROMPT}]

    history = session_store[session_id]
    history.append({"role": "user", "content": message})

    try:
        extra_params = get_extra_params(MODEL)
        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            stream=False,
            temperature=1.0,
            max_tokens=2048,
            **extra_params,
        )
        assistant_msg = response.choices[0].message
        history.append({"role": assistant_msg.role, "content": assistant_msg.content})
        return assistant_msg.content
    except Exception as e:
        print(f"调用 LLM 失败：{e}")
        # 回滚刚才追加的 user 消息，避免污染历史
        history.pop()
        return None


def main():
    messages = [{"role": "system", "content": "Python 学习导师。"}]
    print("多轮对话已启动，输入 exit/quit/退出 结束对话。\n")

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() in ("exit", "quit", "退出"):
            print("对话结束。")
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        response = invoke_llm(messages)
        if response is None:
            continue

        print(f"Assistant: {response.choices[0].message.content}\n")


if __name__ == "__main__":
    main()
