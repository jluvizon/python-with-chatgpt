import openai

openai.api_key = "your-api-key-here"

response = openai.ChatCompletion.create(
    model="gpt-4",  # Assuming 'gpt-4' is the latest model you are referring to
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello World!"}
    ]
)