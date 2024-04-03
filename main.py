from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful teacher."},
        {
            "role": "user",
            "content": "Are there other measures than time complexity for an \
            algorithm?",
        },
        {
            "role": "assistant",
            "content": "Yes, there are other measures besides time complexity \
            for an algorithm, such as space complexity.",
        },
        {"role": "user", "content": "What is it?"},
    ],
)
print(response.choices[0].message.content)