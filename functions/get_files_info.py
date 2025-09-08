import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.config import *
    

def get_files_info(working_directory, directory="."):
    try:
        output=""
        abs_wd=os.path.abspath(working_directory)
        dir=os.path.abspath(os.path.join(abs_wd, directory))
        if directory==".":
            output="Result for current directory: \n"
        else:
            output=f"Result for '{directory}' directory: \n"
        if not dir.startswith(abs_wd):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(dir):
            return f'Error: "{directory}" is not a directory'
        for file in os.listdir(dir):
            output += f'- {file}: file_size={os.path.getsize(dir+'/'+file)} bytes, is_dir={os.path.isdir(dir+'/'+file)} \n'

        return output
    except Exception as e:
        print(f"ERROR:{e}")
        return f"ERROR: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)