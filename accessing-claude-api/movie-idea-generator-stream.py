from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"

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
    with client.messages.stream(
        model=model,
        max_tokens=1000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_input}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print()
    print("---")
