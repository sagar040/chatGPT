#/usr/bin/env python3
#
# Author: Sagar Biswas (sagar040)
#
# https://github.com/sagar040/chatGPT
#
# Version 2.0

import style.ColorCode as c
import random


color_list = [c.r, c.g, c.y, c.b, c.m, c.c, c.lr, c.lg, c.ly, c.lb, c.lm, c.lc]


def banner(c1, c2):
    print(f"""
  {c1}        __          __  {c2}__________  ______
  {c1}  _____/ /_  ____ _/ /_{c2}/ ____/ __ \/_  __/
  {c1} / ___/ __ \/ __ `/ __/{c2} / __/ /_/ / / /
  {c1}/ /__/ / / / /_/ / /_/{c2} /_/ / ____/ / /
  {c1}\___/_/ /_/\__,_/\__/{c2}\____/_/     /_/

                {c.e}ChatGPT API by sagar040\n""")

def random_color():
    return random.choice(color_list)


def print_banner():
    color1 = random_color()
    color2 = random_color()
    banner(color1, color2)