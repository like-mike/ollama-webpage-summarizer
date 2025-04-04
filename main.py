# main.py

import ollama
from website import Website

MODEL = "llama3.2"

SYSTEM_PROMPT = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
    please provide a short summary of this website in markdown. \
    If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

def messages_for(website):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def summarize(website):
    ed = Website(website)
    messages = messages_for(ed)
    response = ollama.chat(model=MODEL, messages=messages)
    return response['message']['content']

if __name__ == "__main__":
    print(summarize("https://miker1012.com"))

