import os
import openai
import dotenv
dotenv.load_dotenv();
api_key=os.getenv("OPENROUTER_API_KEY")
model_mame=os.getenv("LLM_MODEL")
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key)
user_input = input("Enter your message: ")
message = [
{"role": "system", "content": "You are a friendly teacher. Use simple English and answer in no more than three sentences."},   
{"role": "user", "content": user_input}
]
message.append({"role": "user", "content": user_input})
try:
    response = client.chat.completions.create(
        model=model_mame,
        messages=message,
        max_tokens=150
    )
    print("Response from the model: ")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")