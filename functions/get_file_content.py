import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.config import *

def get_file_content(working_directory, file_path):
    try:
        abs_wd=os.path.abspath(working_directory)
        file=os.path.abspath(os.path.join(abs_wd, file_path))
        if not file.startswith(abs_wd):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file):
            f'Error: File not found or is not a regular file: "{file_path}"'
        f = open(file).read()
        if len(f)>char_limit:
            f=f[:char_limit+1:]
            f+=f'[...File "{file_path}" truncated at {char_limit} characters]'
        return f        
    except Exception as e:
        print(f"ERROR:{e}")
        return f"ERROR: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads the contents of a file. if the file is over {char_limit} long, it will truncate at {char_limit}, removing any data that comes after that character number.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read from, relative to the working directory. If not provided, the function will not run.",
            ),
        },
    ),
)