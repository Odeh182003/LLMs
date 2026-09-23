#in this project I give the full chat history to the prompt to make it stateful. 
# The user can type "reset" to clear the chat history and start a new conversation, 
# or "exit" to quit the program.
import os
import openai
import dotenv
dotenv.load_dotenv();
api_key=os.getenv("OPENROUTER_API_KEY")
model_name=os.getenv("LLM_MODEL")
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key)
message = [
{"role": "system", "content": "You are a friendly teacher. Use simple English and answer in no more than three sentences."},
]
user_input = input("Enter your message: ")
while user_input.lower() != "exit":
    if user_input.lower() == "reset":
        message = [
            {"role": "system", "content": "You are a friendly teacher. Use simple English and answer in no more than three sentences."},
        ]
        print("Conversation has been reset.")
        user_input = input("Enter your message: ")
        continue
    message.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
        model=model_name,
        messages=message,
        max_tokens=150
    )
        assistant_reply = response.choices[0].message.content
        print("\nResponse from the model: ")
        print(assistant_reply)
        message.append({"role": "assistant", "content": assistant_reply})
    except Exception as e:
        print(f"An error occurred: {e}")
    user_input = input("\nEnter your message (or type 'exit' to quit, 'reset' to start over): ")