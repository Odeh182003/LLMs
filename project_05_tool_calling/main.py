import json
import os
import openai
import dotenv
from pathlib import Path

dotenv.load_dotenv();
api_key=os.getenv("OPENROUTER_API_KEY")
model_name=os.getenv("LLM_MODEL")
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key)

file_path = "C:/Users/SS/Downloads/llms_mini_projects/llms_mini_projects/shared/fixtures/tool_data.json"
#I need the reference inside lookup_shipment function to be from the tool_data.json file. I will read the json file and pass it to the prompt as a string.
with open(file_path, "r") as file:
    json_data = file.read()

def lookup_shipment(shipment_id):
   data = json.loads(json_data)
   shipment = data.get("shipments", {})
   if shipment_id in shipment:
         return json.dumps(shipment[shipment_id])
   return json.dumps({"error": "Shipment ID not found."})
def list_file():
    return [item.name for item in Path("C:/Users/SS/Downloads/llms_mini_projects/llms_mini_projects/shared/files").iterdir() if item.is_file()]  
def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()
user_input = input("Enter your message: ")
message = [
    {"role": "system", "content": "You are a helpful assistant that can look up shipment information based on a shipment ID. Use the provided JSON data to find the shipment details."},
   # {"role": "user", "content": f"{user_input}\n\nHere is the shipment data:\n{json_data}"}
   {"role": "user", "content": user_input}
]
#It tells the model that it can use the lookup_shipment tool to get shipment information based
#  on a shipment ID. The model can choose to call this tool if it needs to look up shipment 
# details.
shipment_lookup_tools = {
    "type": "function",
    "function":{
    "name": "lookup_shipment",
    "description": "Look up shipment information based on a shipment ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "shipment_id": {
                "type": "string",
                "description": "The ID of the shipment to look up."
            }
        },
        "required": ["shipment_id"]
    }
    }
}
try:
    response = client.chat.completions.create(
        model=model_name,
        messages=message,
        tools=[shipment_lookup_tools],
        tool_choice="auto",
        max_tokens=150
    )
    response_message = response.choices[0].message
#The model reads user input and decides whether to call the lookup_shipment tool 
# based on the shipment ID provided by the user. 
# If the model calls the tool, it will pass the shipment ID as an argument, 
# and the tool will return the corresponding shipment information from the JSON data. 
# The model can then use this information to generate a final response to the user.
    if response_message.tool_calls:
        print(f"\n[AI Agent requested tool call: {response_message.tool_calls[0].function.name}]")
        function_args = json.loads(response_message.tool_calls[0].function.arguments)
        shipment_id = function_args.get("shipment_id")
        tool_response = lookup_shipment(shipment_id)
        print(f"\n[Tool Response: {tool_response}]")
        message.append({"role": "assistant", "content": response_message.content, "tool_calls": response_message.tool_calls})
        message.append({"role": "function", "name": response_message.tool_calls[0].function.name, "content": json.dumps(tool_response)})
        follow_up_response = client.chat.completions.create(
            model=model_name,
            messages=message,
            max_tokens=150
        )
        print("\n[Final Response from the model: ]")
        print(follow_up_response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
