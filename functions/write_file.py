import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.config import *

def write_file(working_directory, file_path, content):
    try:
        abs_wd=os.path.abspath(working_directory)
        file=os.path.abspath(os.path.join(abs_wd, file_path))
        if not file.startswith(abs_wd):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        with open(file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"ERROR:{e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes data to a file, overwriting any existing data in the process. if the directory path does not exist, it creates the directory(ies) and the file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to save the data to, relative to the working directory. If not provided, the function will not run.",
            ),
            "content": types.Schema(
            type=types.Type.STRING,
            description="The content you want to save to the file"
            )
        },
    ),
)