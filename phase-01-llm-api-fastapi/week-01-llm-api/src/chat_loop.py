import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 1. 校验环境变量
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL = os.getenv("LLM_MODEL")

if not all([API_KEY, BASE_URL, MODEL]):
    print("错误：请确保 .env 文件中定义了 LLM_API_KEY, LLM_BASE_URL, LLM_MODEL")
    sys.exit(1)

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 2. 根据模型决定是否添加推理参数
def get_extra_params(model: str):
    """为推理模型添加额外参数"""
    extra = {}
    if "reasoner" in model.lower():  # 假设模型名包含 'reasoner' 即推理模型
        extra["reasoning_effort"] = "high"
        extra["extra_body"] = {"thinking": {"type": "enabled"}}
    return extra

def invoke_llm(messages):
    try:
        extra_params = get_extra_params(MODEL)
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=False,
            temperature=1.0,
            max_tokens=2048,
            **extra_params
        )
        # 将助手回复添加到历史（推荐显式提取）
        assistant_msg = response.choices[0].message
        messages.append({"role": assistant_msg.role, "content": assistant_msg.content})
        return response
    except Exception as e:
        print(f"调用 LLM 失败：{e}")
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
            continue  # 已打印错误，继续下一轮

        print(f"Assistant: {response.choices[0].message.content}\n")

if __name__ == "__main__":
    main()