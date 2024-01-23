from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "I am student in college. How can i start bisness in Ukraine without money?"},
  ]
)


print(response.choices[0].message.content)
