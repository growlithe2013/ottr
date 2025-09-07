from functions.get_files_Info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_py_file import *


print(
run_py_file("calculator", "main.py"),'\n',
run_py_file("calculator", "main.py", ["3 + 5"]),'\n',
run_py_file("calculator", "tests.py"),'\n',
run_py_file("calculator", "../main.py"),'\n',
run_py_file("calculator", "nonexistent.py")
)