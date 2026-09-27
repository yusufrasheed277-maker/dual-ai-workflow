import anthropic
import openai
import json
import os

# Setup
client_anthropic = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "اكتب قصة قصيرة عن مغامرة في الفضاء"

# Claude API
print("🔵 استدعاء Claude...")
claude_response = client_anthropic.messages.create(
    model="claude-opus-4-1",
    max_tokens=500,
    messages=[
        {"role": "user", "content": prompt}
    ]
)
claude_text = claude_response.content[0].text

# OpenAI API
print("⚪ استدعاء ChatGPT...")
gpt_response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=500
)
gpt_text = gpt_response.choices[0].message.content

# حفظ النتائج
os.makedirs("results", exist_ok=True)

results = {
    "claude": {
        "model": "claude-opus-4-1",
        "response": claude_text
    },
    "chatgpt": {
        "model": "gpt-4",
        "response": gpt_text
    }
}

with open("results/ai_comparison.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("✅ تم حفظ النتائج في results/ai_comparison.json")
