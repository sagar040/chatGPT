#!/usr/bin/env python3

import os
import sys
import openai
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

try:
    import api.conf as conf
except ModuleNotFoundError:
    print("\033[31mrun setup.sh first !\033[0m")
    sys.exit(1)
    

banner = """\033[34;1m
      _           _    ____ ____ _____ 
  ___| |__   __ _| |_ / ___|  _ \\_   _|
 / __| '_ \\ / _` | __| |  _| |_) || |  
| (__| | | | (_| | |_| |_| |  __/ | |  
 \\___|_| |_|\\__,_|\\__|\\____|_|    |_|  
                                       \033[0m"""

Msg_clear_screen = "\n\033[33mclear\033[0m - clear the screen"
Msg_save = "\n\033[33msave\033[0m - save the current output"
Msg_exit = "\n\033[33mCTRL+C\033[0m - exit the program"

API_KEY = conf.key

def run(key,quarry):
    openai.api_key = key
    
    completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=quarry,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )
    return completions.choices[0].text

def save(data):
    with open("output.txt","w") as f:
        f.write(data)


def search_language(text):
  languages = ["c++", "c#", "css", "html", "javascript", "json", "python", "sql", "xml", "php", "java", "bash", "sh", "powershell", "go"]
  for language in languages:
    if language in text:
      return language
  return "text"


print(banner, Msg_clear_screen, Msg_save, Msg_exit, "\n")

while True:
    try:
        you = input("\033[32;1m>>\033[0m ")
        if you == "clear":
            os.system("clear")
        elif you == "save":
            save(output)
            print("[ output is saved in 'output.txt' file ]\n")
        elif you == "":
            pass
        else:
            try:
                output = run(API_KEY,you)
                syntax = search_language(you)
                print(f'\n{highlight(output, lexer=get_lexer_by_name(syntax), formatter=Terminal256Formatter(style="monokai"))}')
            except openai.error.AuthenticationError as e :
                print(f"\033[31;1mE:\033[0m {e}")
                print("run setup.sh file to set api key")
    except KeyboardInterrupt:
        print("\n\033[31;1mBye..!\033[0m")
        break
