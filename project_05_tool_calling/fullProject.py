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
         return shipment[shipment_id]
   return {"error": "Shipment ID not found."}
SHARED_FILES_DIR = Path("C:/Users/SS/Downloads/llms_mini_projects/llms_mini_projects/shared/files")
def list_file():
    return [item.name for item in Path("C:/Users/SS/Downloads/llms_mini_projects/llms_mini_projects/shared/files").iterdir() if item.is_file()]  
def read_file(file_name):
    if ".." in file_name or Path(file_name).is_absolute():
        return "Invalid file name. Please provide a valid file name within the shared/files directory."
    if not file_name.endswith((".txt", ".md")):
        return "Invalid file type. Only .txt and .md files are allowed."
    target_file_path = (SHARED_FILES_DIR/file_name).resolve()
    if not str(target_file_path).startswith(str(SHARED_FILES_DIR.resolve())):
        return "Invalid file name. Please provide a valid file name within the shared/files directory."
    if not target_file_path.exists() or not target_file_path.is_file():
        return "File not found. Please provide a valid file name within the shared/files directory."
    with open(target_file_path, "r", encoding="utf-8") as file:
        return {"content": file.read()}
user_input = input("Enter your message: ")
message = [
    {
        "role": "system", 
        "content": (
            "You are a helpful assistant with access to tools to look up shipments and read files. "
            "When a user asks a question, first check the available files using list_file. "
            "Then, use read_file to check files that might contain the answer. "
            "If the information is NOT in the files, you must state clearly that you do not know "
            "and never hallucinate answers."
        )
    },
    {"role": "user", "content": user_input}
]
#It tells the model that it can use the lookup_shipment tool to get shipment information based
#  on a shipment ID. The model can choose to call this tool if it needs to look up shipment 
# details.
tools = [
{
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
},
{
"type": "function",
    "function":{
    "name": "list_file",
    "description": "List all files in the shared/files directory.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
    }
},{ "type": "function",
    "function": {
    "name": "read_file",
    "description": "Read the content of a specified file in the shared/files directory.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string",
                "description": "The name of the file to read."
            }
        },
        "required": ["file_name"]
    }
    }
}

]   
try:
    response = client.chat.completions.create(
        model=model_name,
        messages=message,
        tools=tools,
        tool_choice="auto",
        max_tokens=300
    )
    response_message = response.choices[0].message

    if response_message.tool_calls:
        message.append(response_message)
        for tool_call in response_message.tool_calls:
            tool_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            print(f"\n[AI Agent requested tool call: {tool_name}]")
            if tool_name == "lookup_shipment":
                shipment_id = function_args.get("shipment_id")
                tool_response = lookup_shipment(shipment_id)
            elif tool_name == "list_file":
                tool_response = list_file()
            elif tool_name == "read_file":
                file_name = function_args.get("file_name")
                tool_response = read_file(file_name)
            else:
                tool_response = {"error": "Unknown tool requested."}
            print(f"\n[Tool Response: {tool_response}]")
            message.append({"role": "tool","tool_call_id": tool_call.id, "name": tool_name, "content": json.dumps(tool_response)})
            follow_up_response = client.chat.completions.create(
                model=model_name,
                messages=message,
                max_tokens=300
            )
            print("\n[Final Response from the model: ]")
            print(follow_up_response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")
