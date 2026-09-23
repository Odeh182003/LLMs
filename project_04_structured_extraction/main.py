import ijson
import os
import openai
import dotenv
import json
from decimal import Decimal




dotenv.load_dotenv();
api_key=os.getenv("OPENROUTER_API_KEY")
model_name=os.getenv("LLM_MODEL")
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key)
file_path = "C:/Users/SS/Downloads/llms_mini_projects/llms_mini_projects/shared/fixtures/extraction_cases.json"

with open(file_path, "r") as file:
    json_objects = ijson.items(file, "item")
    first_json = next(json_objects)
input_text = first_json["input"]
print(f"Analyzing text: \"{input_text}\"\n")
message = [
    {"role": "system", "content": "You are a data extraction assistant. Extract the required fields from the provided text and return it in JSON format. For missing fields or null fields, return null. Do not include any additional text or explanations. I want the returned JSON to be valid and parsable. The required fields are: 'document_type', 'document_number', 'organization', 'document_date','currency','total'."},
    {"role": "user", "content": input_text}
]
try:
    response = client.chat.completions.create(
        model=model_name,
        messages=message,
        max_tokens=300
    )
    response_content = response.choices[0].message.content
    if not response_content:
        print("Friendly Error: The model returned an empty response. Please try running it again!")
    else:
        raw_response_content = response_content.strip()
        print("Raw Response from the model:\n", raw_response_content)
        try:
            parsed_response = json.loads(raw_response_content)
            print("\nParsed JSON Response:\n", json.dumps(parsed_response))
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print("The model's response was not valid JSON. Please check the output above for details.")
except Exception as e:
    print(f"An error occurred: {e}")