import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"))
messages =[{"role": "system", "content": "Python 学习导师。"}]


    

def invoke_llm(messages):
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=messages,
        stream=False,
        temperature=1,
        max_tokens=2048,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    messages.append(response.choices[0].message)
    return response
def main():    
    while True:
        user_input=input("User: ")
        if user_input == "exit":
            break
        messages.append({"role": "user", "content": user_input})
        response = invoke_llm(messages)
        
        print(response.choices[0].message.content)    
    
    
    
if __name__ == "__main__":
    main()
    