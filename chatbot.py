from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-opus-4-7"

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages):
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=messages,
        cache_control={"type": "ephemeral"},
    )
    return response.content[0].text

messages = []

while True:
    user_input = input("> ")
    if user_input.strip().lower() in ("quit", "exit"):
        break

    print("---")
    add_user_message(messages, user_input)
    response = chat(messages)
    add_assistant_message(messages, response)
    print(response)
    print("---")
