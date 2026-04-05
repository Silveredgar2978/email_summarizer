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