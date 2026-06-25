import os
from dotenv import load_dotenv
from openai import OpenAI
from prompt_templates import SYSTEM_PROMPT

def main():
    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"))

    question = input("Please enter your question:")
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.get("history_expert")},
            #{"role": "system", "content": SYSTEM_PROMPT.get("medical_expert")},
            {"role": "user", "content": question},
        ],
        stream=False,
        temperature=1.0,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    print(response.choices[0].message.content)
    
if __name__ == "__main__":
    main()