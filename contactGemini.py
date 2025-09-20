#contactGemini.py

import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_file_content import *
from functions.get_files_info import *
from functions.write_file import *
from functions.run_py_file import *
from config import *

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")

messages = []

client = genai.Client(api_key=api_key)
system_prompt =  """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

if you call a function, do not send text. just respond with the function call.
do not explain what you are doing, just send the calls.
if you do not call a function you may send text.
"""

def call_function(function_call_part, verbose=False):
    dispatch = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_py_file": run_py_file,
    "write_file": write_file
    }
    if verbose:
        print(f"calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Calling function: {function_call_part.name}")
    fn = dispatch.get(function_call_part.name)
    print(fn(working_directory, **function_call_part.args))
    return fn(working_directory, **function_call_part.args)

def contactGemini(message="", verbose=False, caller="main"):

    
    if caller=="Gemini":
        print("Reiterating.")
    available_functions = types.Tool(function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_py_file,
        schema_write_file
    ])
    global client
    response=[]
    global messages
    user_prompt=message
    if message != None:
        if isinstance(message, str):
            messages.append(types.Content(role="user", parts=[types.Part(text=message)]))
    response.append(client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        ))
    for candid in response[-1].candidates:
        messages.append(candid.content)
    if response[-1].function_calls:
        messages.append(
        types.Content(role="user", parts=[types.Part(text=str(call_function(response[-1].function_calls[-1], verbose)))]))

    return response[-1]