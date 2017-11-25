import os

print("1. Language Translator\n2. Personality Insights\n3. Conversation\n\n")
selection = raw_input("Your Choice: ")

if selection == '1':
    text = raw_input("Your Text: ")
    src = raw_input("Given Language: ")
    dest = raw_input("Translated into: ")
    #call language translator
    command = "python lang_translator.py '" + text + "' " + src + " " + dest
    os.system(command)

elif selection == '2':
    #call personality insights
    raw_input("How was your day?\n")
    command = "python pi.py"
    os.system(command)

elif selection == '3':
    #call conversation
    textgot = raw_input("Say: ")
    command = "python conversation.py '" + textgot + "'"
    os.system(command)
