# BUSINESS EMAIL SUMMARIZER
# -------------------------
# Build a tool that does all of this:
#
# 1. Reads a .txt file that contains an email
#    - The filename should be typed by the user in the terminal
#    - If the file doesn't exist, handle that error and ask again
#
# 2. Sends the email content to Gemini with a system prompt:
#    "You are a professional assistant. Summarize this business email
#     in 3-5 bullet points. Focus on key information, action items,
#     and deadlines."
#
# 3. Prints the summary clearly in the terminal
#
# 4. Asks the user if they want to summarize another email
#    - If yes, loop back
#    - If no, exit cleanly
#
# REQUIREMENTS:
# - Read the email from a real .txt file
# - Use Gemini with a system prompt
# - Use functions — do not write everything in one block
# - Handle errors: file not found, empty file, API errors
# - Load API key from .env
# - Code must be clean and commented

import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()   #gets the api key in .env
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

#calls all functions, and establishes main loop
def main():
    print("Welcome to the email summarizer", end="\n\n")
    while True:
        print()
        question_input = input("Do you want to summarize an email? \"y\" (yes) \"n\" (no): ")
        if question_input.strip() == "y":
            print()
            print(summarize_mail(ask_mail(), "You are a professional assistant. Summarize this business email in 3-5 bullet points. Focus on key information, action items, and deadlines."))

        elif question_input.strip() == "n":     #if user doesn't want to summarize an email
            print()
            print("Have a good day")
            break
        else:                                   #if any other letter/no letter is placed
            print()
            print("enter a valid option")
            continue
        
#asks for file and retrieves the information as a text
def ask_mail():
    while True:
        try:
            print()
            file_name = input("What is the file name? ")
            print()
            with open(file_name, "r") as mail:
                content =  mail.read()          #gets the text from the file
                if content.strip() == "":       #checks if file is empty, and re-runs loop if empty
                    print("this file is empty")
                    continue
                return content
        except FileNotFoundError:       #handles error if file doesn't exist
            print()
            print("this is not a file bitch, make sure its in the folder")
            continue        #continues loop


#makes the call to gemini, with the content of the mail and the prompt (instructions to summarize)
def summarize_mail(mail_content, prompt):
    try:
        response = client.models.generate_content(                  #uses free model, adds system prompt configuration
            model="gemini-2.5-flash",                               #establishes the instructions and the gives mail content
            config=types.GenerateContentConfig(
                system_instruction=prompt),
            contents=mail_content
        )
        return response.text        #returns summary to main function to print
    except Exception as e:      #handles errors by GEMINI
        print()
        print(f"There was an error: {e}")   #e shows the error
        return      #returns nothing to get back to main function
    
main()      #calls the main function
