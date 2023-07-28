#!/usr/bin/env python3
import ai
import openai
import os

# Set up your OpenAI API credentials
# For some reason you sometimes need both of these lines
os.environ["OPENAI_API_KEY"] = "your-key-here"
openai.api_key = "your-key-here"

# Initialize the AI object as "myai"
myai = ai.AI()

while True:
    # Example usage:
    user_prompt = input("Enter a prompt: ")
    print(myai.get_response_to_prompt(user_prompt))
