from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"
temperature = 0.0

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

messages = []

system_prompt = """
You are a creative movie idea generator.
When the user describes a concept, genre, theme, or any prompt,
generate an original and compelling movie idea in exactly 3 sentences.
Be imaginative and explore unexpected angles.
"""

while True:
    user_input = input("> ")
    if user_input.strip().lower() in ("quit", "exit"):
        break

    print("---")
    add_user_message(messages, user_input)
    response = chat(messages, system=system_prompt, temperature=temperature)
    add_assistant_message(messages, response)
    print(response)
    print("---")
