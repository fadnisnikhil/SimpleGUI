import easygui as eg
import sys
import re

question = "This is your question"
title = "This is your window title"
listOfOptions = ["option 1", "option 2", "option 3"]

choice = eg.multchoicebox(question, title, listOfOptions)
print(choice)
ch=[]
for element in choice:
    ch1 = element.strip().split(" ")[1]
    ch.append(ch1)
print(ch)
if "1" in ch:
    print("Option 1 selected")
if "2" in ch:
    print("Option 2 selected")
if "3" in ch:
    print("Option 3 Selected")
else:
    print("No option selected")


