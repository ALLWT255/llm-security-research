from ollama import chat

response = chat(
    model="llama3:latest",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: Ollama connection successful"
        }
    ]
)

print(response.message.content)