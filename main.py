# General Libraries
# installing Natural Language Toolkit which processes the language spoken by Humans.
# AI+++++++++++++++++++++++++++++++++++

import nltk

# speech
from gtts import gTTS

# This module is imported so that we can play
# converted into audio
import os
import random

# AI+++++++++++++++++++++++++++++++++++++++

# This tokenizer divides a text into a list of sentences
nltk.download('punkt')
# imports the "namespace" Tkinter in your namespace and import Tkinter as tk does the same, but "renames" it locally
# to 'tk' to save you typing
import tkinter as tk
# imports every exposed object in Tkinter into your current namespace.
from tkinter import *
# Specific GUI Window Tabs Libraries
# Several ttk widgets will automatically substitute for the Tk widgets. Direct benefit of using the new widgets,
# giving better look & feel across platforms.
from tkinter import PhotoImage

# Produces a functional scroll bar in a text widget
from tkinter.scrolledtext import *
# imported class SummerTime from the file SummerTime
from SummerTime import SummerTime

# speech
# from gtts import gTTS


# window is built named window2 (intro)

# 2nd window being build
window = tk.Tk()

# window Title has been named
window.title("Sally The AI")

# Change Window Size Here
# wide x tall

window.geometry('700x850')

# Change Text color here
window.config(background='#9B30FF')

# Add/Remove Window Tabs Here

# icon images+++++++++++++++++++++++++++++++++
trashIcon = PhotoImage(file="trash.png")
# size image
trash = trashIcon.subsample(2, 2)
# image of Sally
aiIcon = PhotoImage(file="Sally.png")
sally = aiIcon.subsample(1, 1)
ai = Label(window, image=sally, padx=25, pady=25, bg="orange")
ai.grid(column=4, row=1)
# +++++Speaker++++++++
speakIcon = PhotoImage(file="speaker.png")
# size image
speaks = speakIcon.subsample(2, 2)
# +++++summary++++++++
sumIcon = PhotoImage(file="sumup.png")
# size image
sumUp = sumIcon.subsample(2, 2)

labelIcon = PhotoImage(file="label.png")
labelOne = labelIcon.subsample(2, 3)

labelIcon2 = PhotoImage(file="label1.png")
labelTwo = labelIcon2.subsample(2, 3)

# a label widget is created for the window with text 'Enter text to Summarize'
label_text_to_summarize1 = Label(window, image=labelTwo, padx=35, pady=35)
# label was placed using .grid
label_text_to_summarize1.grid(row=8, column=1)
# ++++++++++++++++++++++++++++++++++++++++++

# Set style of tabs
# ttk.Style May be used to specify a custom widget style
# style =   'window' is now able to be stacked with widgets ttk.Style()

# GUI


# label widget with a notebook widget with a rectangular container with text with padding
label_summarize = Label(window,
                        text="\nHi, I am Textatron. Let me read and then Summerize the text. Then you may review and "
                             "edit.\n",
                        padx=5, pady=5)


# AI++++++++++++++++++++++
# ai is created
def ai_creator():
    # generated random sayings+++++++++++++++++++++++++
    SallyHelpSayings = ['Watch me work ']
    sallyhelped = random.choice(SallyHelpSayings)
    # ++++++++++++++++++++++++++++++++++++++++++++++++
    language = 'en'
    # Passing the text and language and text to the engine
    # here we have slow = False. which tells the
    # module that the converted audio should
    # have high speed
    myobj = gTTS(text=sallyhelped, lang=language, slow=False)  # Create a list that randomizes output
    # saving the converted audio in mp3 file named
    # welcome
    myobj.save("aiSpeaking.mp3")
    # Playing the converted file
    os.system("start aiSpeaking.mp3")


def ai_speak():
    # generated random sayings+++++++++++++++++++++++++
    SallyTalking = ['Hello']
    sallytalks = random.choice(SallyTalking)
    file = open("ai.txt", "w")
    # ai writes output in a file
    file.write(sallytalks)
    # closes file
    file.close()
    myText2 = open("ai.txt", "r").read().replace("\n", " ")
    # language
    language = 'en'
    myobj = gTTS(text=myText2, lang=language, slow=False)  # Create a list that randomizes output
    # saving the converted audio in mp3 file named
    # welcome
    myobj.save("aiSpeaking1.mp3")
    # Playing the converted file
    os.system("start aiSpeaking1.mp3")


# deletes input
def erase_input():
    entry.delete('1.0', END)
    output_display.delete('1.0', END)
    erase_input()


# a defined function name summer_time from the SummerTime.py
def summer_time():
    ai_creator()
    # Imports for parser_config
    # sumy is a paragraph summarizer
    # import PlaintextParser allows data to be read
    from sumy.parsers.plaintext import PlaintextParser
    # import Tokenizer converts input text to streams of tokens, where each token is a separate word
    from sumy.nlp.tokenizers import Tokenizer
    # text_format = user input
    text_format = entry.get(f'1.0', tk.END)
    # parser_config = user text/that is im english
    parser_config = PlaintextParser.from_string(text_format, Tokenizer(f"english"))
    # summerTime = the class SummerTime() from file SummerTime.py
    summerTime = SummerTime()
    # summer_all = the a algorithm that summarizes text
    summer_all = summerTime.lex_rank_analysis(parser_config, 2)
    # summer_all = print(), summer_all
    # summer_all = the a algorithm that summarizes text
    summer_all = summer_all + summerTime.luhn_analysis(parser_config, 1)
    # summer_all = print(), summer_all
    # summer_all = the a algorithm that summarizes text
    summer_all = summer_all + summerTime.lsa_analysis(parser_config, 1)
    # a list was created
    scrubbed = []
    # 3 different algorithms is broken down into their own sentences
    for sentence in summer_all:
        concat = str(sentence) + f"\n "
        concat.replace(f"", "   ")
        scrubbed.append(concat)
    #TODO output to GUI
    # insert 3 sentences into the output_display scrolled_text widget
    output_display.insert(tk.END, scrubbed)
    print(f"\nAbout to print summer all results\n")
    print(summer_all)


####GUI###############################################


# a label widget is created for the window with text 'Enter text to Summarize'
label_text_to_summarize = Label(window, image=labelOne, padx=25, pady=25)
# label was placed using .grid
label_text_to_summarize.grid(row=1, column=1)

# entry = a scrolled text widget for the window used to accept user input
entry = ScrolledText(window, wrap=WORD, height=5)
# location of the scrolled text widget using .grid
entry.grid(row=2, column=1, columnspan=5, padx=25, pady=25)

# User Action Controls and Events

# Main button
button_run1 = Button(window, text="Sally Summarize", command=summer_time, image=sumUp, width=70, height=70, bg='orange',
                     fg='#fff')
# button is placed and sized using .grid
button_run1.grid(row=0, column=1, padx=10, pady=10)

# Copy button
# button widget created with text 'Invoke Text-A-Tron'
# button_run = Button(window, text="copy clip", command='', width=22, bg='#25d366', fg='#fff')
# button is placed and sized using .grid
# button_run.grid(row=4, column=2, padx=10, pady=10)

# button widget created with text 'Erase Input'
button_erase_input = tk.Button(window, text='Sally Erase OutPut', image=trash, command=erase_input, width=70, height=70,
                               bg='orange', fg='#fff')
button_erase_input.grid(row=0, column=3, padx=10, pady=10)

# button widget created for Speak
button_erase_output = Button(window, text='Speak', image=speaks, command=ai_speak, width=70, height=70, bg='orange',
                             fg='#fff')
# button is placed using .grid
button_erase_output.grid(row=0, column=2, padx=10, pady=10)

# Display window for summarization results
output_display = ScrolledText(window, wrap=WORD, height=20)
# output_display is placed using .grid
output_display.grid(row=9, column=1, columnspan=5, padx=5, pady=5)

# Keep window alive
window.mainloop()
