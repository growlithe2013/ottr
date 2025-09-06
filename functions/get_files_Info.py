import os
import sys
from functions.config import *

#os.getcwd()
    

def get_files_info(working_directory, directory="."):
    try:
        abs_wd=os.path.abspath(working_directory)
        dir=os.path.abspath(os.path.join(abs_wd, directory))
        if directory==".":
            print("Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")
        if not dir.startswith(abs_wd):
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(dir):
            print(f'Error: "{directory}" is not a directory')
            return f'Error: "{directory}" is not a directory'
        for file in os.listdir(dir):
            print(f'- {file}: file_size={os.path.getsize(dir+'/'+file)} bytes, is_dir={os.path.isdir(dir+'/'+file)}')
            return f'- {file}: file_size={os.path.getsize(dir+'/'+file)} bytes, is_dir={os.path.isdir(dir+'/'+file)}'

        return
    except Exception as e:
        print(f"ERROR:{e}")
        return f"ERROR: {e}"

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