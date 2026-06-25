import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompt_templates import SYSTEM_PROMPT

def main():
    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"))

    print("Please enter your SQL (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    question = "\n".join(lines)
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.get("sql_analyzer")},
            #{"role": "system", "content": SYSTEM_PROMPT.get("medical_expert")},
            {"role": "user", "content": question},
        ],
        stream=False,
        temperature=1.0,
        
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    print(parse_json_response(response.choices[0].message.content))
    
    
def parse_json_response(response):
    result = {
    "success": False,
    "data": None,
    "error": "..."
    }
    try:
        result["data"]=json.loads(response)
        result["success"]=True
        return result
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return result
    
if __name__ == "__main__":
    main()