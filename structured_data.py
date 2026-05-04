
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-5"

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages, stop_sequences=None):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        stop_sequences=stop_sequences,
    )
    return message.content[0].text


messages = []

prompt = "Generate three different sample AWS CLI commands. Each should be very short."

add_user_message(messages, prompt)
add_assistant_message(messages, "Here are all three commands in a single block without any comments:\n```bash")

text = chat(messages, stop_sequences=["```"])
print(text.strip())
