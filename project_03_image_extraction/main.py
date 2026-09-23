import os
import openai
import dotenv
import base64

dotenv.load_dotenv();
api_key=os.getenv("OPENROUTER_API_KEY")
model_name=os.getenv("LLM_MODEL")
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key)
image_path = "C:/Users/SS/Downloads/llms_mini_projects/llms_mini_projects/shared/fixtures/invoice.jpg"
with open(image_path, "rb") as image_file: # rb to read the image in binary mode
    image_data = base64.b64encode(image_file.read()).decode("utf-8") # encode the image data to base64 and decode to string

user_input = input("Enter your message: ")
message = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": user_input},
            {"type": "image_url", "image_url": {"url":f"data:image/jpeg;base64,{image_data}"}}
        ]
    }
]
try:
    response = client.chat.completions.create(
        model=model_name,
        messages=message,
        max_tokens=300
    )
    print("Response from the model: ")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")
