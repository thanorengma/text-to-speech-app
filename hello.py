import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voice = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voice[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voice[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def download():

    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voice = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voice[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voice[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

#frontend/gui###########
root = Tk()
root.title("TEXT TO SPEECH CONVERTER")
root.geometry("900x450+200+200")
root.resizable(False, False)

# configure the size of the app window
root.configure(bg="#28282B")  # setting background color

# bring images at the top bar where the app name is located
image_icon = PhotoImage(file="asonnn.png")
root.iconphoto(False, image_icon)

# dimensions of the top frame
Top_frame = Frame(root, bg="#8FB8DE", width=900, height=100)
Top_frame.place(x=0, y=0)


Logo = PhotoImage(file="toplogo.png")
Label(Top_frame, image=Logo, bg="#28282B").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH CONVERTER",
      font="arial 20 bold", bg="#8FB8DE", fg="black").place(x=100, y=30)

###################

# text field
text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# lable dimension for voice
Label(root, text="VOICE", font="arial 15 bold",
      bg="#305065", fg="white").place(x=580, y=160)
# lable dimension for speed
Label(root, text="SPEED", font="arial 15 bold",
      bg="#305065", fg="white").place(x=760, y=160)

# list for gender
gender_combobox = Combobox(
    root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Female')

# list for speed
speed_combobox = Combobox(
    root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Fast')

# speaker icon
imageicon = PhotoImage(file="speaker1.png")

# play button
btn = Button(root, text="PLAY", compound=LEFT,
             image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)


# download icon
imageicon2 = PhotoImage(file="download.png")

# download button
save = Button(root, text="SAVE", compound=LEFT,
              image=imageicon2, width=130, bg="#ACE894", font="arial 14 bold", command=download)
save.place(x=730, y=280)


root.mainloop()
