#/usr/bin/env python3
#
# Author: Sagar Biswas (sagar040)
#
# https://github.com/sagar040/chatGPT
#
# Version 2.0

import sys
import subprocess
import style.ColorCode as c


def help_menu():
    print(f"""
   Version 2.0
  -------------
  {c.ly}help{c.e}              {c.i}Print this message.{c.e}
  {c.ly}clear{c.e}             {c.i}Clear screen.{c.e}
  {c.ly}save{c.e}              {c.i}Save output.{c.e}
  {c.ly}exit{c.e}              {c.i}Quit the program.{c.e}
""")


def save(input_text, output_text):
    date = subprocess.getoutput("date")
    with open("saved_chat.txt","a") as s:
        s.write(f"# {str(date)}\n")
        s.write(f"{str(output_text)}\n")
        s.write("---- ---- ---- ---- ----\n\n")
    print(f"chat saved at {c.g}{subprocess.getoutput('pwd')}/saved_chat.txt{c.e}")


def syntax(text):
    languages = ["c++", "c#", "css", "html", "javascript", "json", "python", "sql", "xml", "php", "java", "bash", "sh", "powershell", "go"]
    for language in languages:
        if language in text:
           return language
    return "text"