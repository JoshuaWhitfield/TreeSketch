import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
)

def call_deepseek_agent(preprompt, user_input):
    messages = [
        {"role": "system", "content": preprompt},
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=0.3,
        stream=False
    )
    output = response.choices[0].message.content
    return parse_agent_response(output)

import json
import re

def parse_agent_response(output_text):
    try:
        # Strip code block wrappers like ```json ... ```
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", output_text, re.DOTALL)
        if match:
            output_text = match.group(1)

        return json.loads(output_text)

    except json.JSONDecodeError as e:
        print("❌ Error: Invalid JSON response from DeepSeek.")
        print("⚠️ Raw output was:\n", output_text)
        return {
            "structure_string": "",
            "file_contents": {},
            "message": "⚠️ Invalid response format."
        }
