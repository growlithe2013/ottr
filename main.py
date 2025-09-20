#main.py

import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from contactGemini import *
from functions.get_file_content import *
from functions.get_files_info import *
from functions.write_file import *
from functions.run_py_file import *
from config import *


chat=contactGemini

def main():

    verbose=False

    print("Hello from ottr!")

    match (len(sys.argv)):

            
        
        case 2:
            response=[]

            if sys.argv[1].lower() != "--verbose":
                response.append(chat(sys.argv[1]))
                if response[-1].function_calls != None:
                    done=False
                    i=0
                    while done==False and i<20:
                        response.append(chat(None))
                        if response[-1].text != None:
                            done=True
                        i+=1

                print(response[-1].text)
            if sys.argv[1].lower()=="--verbose":
                verbose=True
            

        case 3:
            if sys.argv[2].lower()=='--verbose':
                verbose=True
                response=[]
                response.append(chat(sys.argv[1], True))
                if response[-1].function_calls != None:
                    done=False
                    i=0
                    while done==False and i<20:
                        response.append(chat(None, True))
                        if response[-1].text != None:
                            done=True
                        i+=1

                print(f"\nUser prompt: {sys.argv[1]}")            
                print(f"Final response: {response[-1].text}")
                print(f"\nPrompt tokens: {response[-1].usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response[-1].usage_metadata.candidates_token_count}")
                

    while True:
        if "response" not in locals() or "response" not in globals():
            response=[]
        done=False
        i=0
        if len(response)>19:
            response.pop(0)
        userIn = input("What is your question? Q to quit, S for settings, enter prompt: ")
        if userIn.upper()=="Q":
            sys.exit(0)
        elif userIn.upper()=="S":
            print("There is currently nothing configurable.")
        else:
            while done==False and i<20:
                response.append(chat(userIn, True))
                if response[-1].text != None:
                    done=True
                i+=1
            if verbose==False:
                print(response[-1].text)
            elif verbose == True:
                print(f"\nUser prompt: {userIn}")            
                print(f"Final response: {response[-1].text}")
                print(f"\nPrompt tokens: {response[-1].usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response[-1].usage_metadata.candidates_token_count}")
                    
            




if __name__ == "__main__":
    main()
