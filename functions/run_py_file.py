import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.config import *
import subprocess


def run_py_file(working_directory, file_path, args=[]):

    try:

        abs_wd=os.path.abspath(working_directory)
        file=os.path.abspath(os.path.join(abs_wd, file_path))
        if not file.startswith(abs_wd):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file):
            return f'Error: File "{file_path}" not found.'
        
        if not file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.' 

        process = subprocess.run(args=[sys.executable, file] + args, timeout=30, capture_output=True, cwd=abs_wd, text=True)
        
        if process.stdout != None:
            exit_str = f"STDOUT: {process.stdout} \n STDERR: {process.stderr}"
        
        if process.stdout == None:
            exit_str = "No output produced."

        if str(process.returncode) != '0':
            return f"{exit_str} \n Process exited with code {process.returncode}"
        
        return exit_str
        
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_py_file = types.FunctionDeclaration(
    name="run_py_file",
    description="runs a python script",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file to run, relative to the working directory. If not provided, or if the file is not a python file, the function will not run.",
            ),
            "args": types.Schema(
            type=types.Type.ARRAY,
            description="any arguments that need to be passed into the python script when running the file. These are optional.",
            items=types.Schema(
                type=types.Type.STRING
            )
            )
        },
    ),
)