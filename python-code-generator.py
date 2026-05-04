from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-5"

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 4096,
        "messages": messages,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

messages = []

system_prompt = "You are a Python engineer who writes very concise code."

while True:
    user_input = input("> ")
    if user_input.strip().lower() in ("quit", "exit"):
        break

    print("---")
    add_user_message(messages, user_input)
    response = chat(messages, system=system_prompt)
    add_assistant_message(messages, response)
    print(response)
    print("---")
