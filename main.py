import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from contactGemini import *




chat=contactGemini

def main():

    print("Hello from ottr!")

    match (len(sys.argv)):
        case 1:
            print("Please give a request for Gemini. EG: python main.py 'prompt here'")
            sys.exit(1)
        
        case 2:
            print(chat(None))
            return

        case 3:
            if sys.argv[2]=='--verbose':
                response=[]
                response.append(chat(None))
                print(f"\nUser prompt: {sys.argv[1]}")
                print(f"\nAnswer: {response[-1].text}")
                print(f"\nPrompt tokens: {response[-1].usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response[-1].usage_metadata.candidates_token_count}")
                sys.exit(0)
            print("Unknown options. Correct usage: main.py 'prompt' --verbose(optional)")
            sys.exit(1)


if __name__ == "__main__":
    main()
