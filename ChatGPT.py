#!/usr/bin/env python3
#
# Author: Sagar Biswas (sagar040)
#
# https://github.com/sagar040/chatGPT
#
# Version 2.0

from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter
from pygments import highlight
import style.banner as banner
import style.ColorCode as c
import Core.process as ps
import readline
import openai
import sys
import os

try:
    import api.conf as conf
except ModuleNotFoundError:
    print("run setup.sh first !")
    sys.exit(1)

banner.print_banner()

def api(text):
    completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )
    return completions.choices[0].text


def prompt():
    while True:
        try:
            text = input(f"{c.ul}ChatGPT{c.e} > ")
            print(c.e)
            if text == "help":
                ps.help_menu()
            
            elif text == "clear":
                os.system("clear")
            
            elif text == ("save"):
                try:
                    ps.save(text,resp)
                except UnboundLocalError:
                    print(f"{c.r}E:{c.e} Nothing to save")
            
            elif text == "exit":
                sys.exit(0)
            
            elif not text:
                pass
            
            else:
                try:
                    resp = api(text)
                    
                    final_syntax = ps.syntax(text)
                    
                    if final_syntax == "text":
                        final_syntax = ps.syntax(resp)
                    
                    print(f'{highlight(resp, lexer=get_lexer_by_name(final_syntax), formatter=Terminal256Formatter(style="monokai"))}')
                
                except openai.error.AuthenticationError as e :
                    print(f"{c.r}E:{c.e} {e}")
        
        except KeyboardInterrupt:
            print(f"{c.r}Exit..{c.e}")
            sys.exit(1)


openai.api_key = conf.key

if openai.api_key:
    prompt()
else:
    print(f"{c.r}E:{c.e} API key not set, run setup.sh file.")