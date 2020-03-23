from tkinter import *
import time
from threading import Timer
import threading
#Generate base window
master = Tk()
    #Canvas
C = Canvas(master, bg='grey',height=600,width=400)
C.pack()
anger = 0
happy = 0
question = 0

def interface():
    # C.create_window(window=introtext)
    introtext.place(x=10, y=10)
    introtext.insert(1.0, 'Welcome to...\nThe Personal and Very Customized quiz-night!\n*cheering* Press a button. Any button! \n(The only button)')
    introtext.config(state=DISABLED)
    # print("it's working, ITS WORKING!")


def begin():
    starttext = Text(master, width=45, height=5)
    starttext.place(x=10,y=10)
    starttext.insert(1.0, 'What I want you to do is... To answer every \nquestion honestly. \nI dont want to see you pressing any "random \nbuttons", got it?')
    C.delete(a)
    C.create_window(200,120,window=accept_and_start_btn)
    C.update()

def incorrect():
    global anger
    global question
    anger=anger +1
    incorrect_msg = Text(master, width=45, height=5)
    incorrect_msg.place(x=10,y=10)
    if anger == 1:
        incorrect_msg.insert(1.0, "Oh no. You didn't actually know the answer?")
    if anger == 2:
        incorrect_msg.insert(1.0, "Another answer you didn't know, huh?")
    if anger == 3:
        incorrect_msg.insert(1.0, "OF COURSE you didn't know the answer! Why do I even bother with you?")
    C.update
    if question == 1:
        timer_sec_que.start()
    if question == 2:
        timer_thi_que.start()
    if question == 3:
        timer_fou_que.start()

def correct():
    global happy
    global question
    happy = happy +1
    correct_msg = Text(master, width=45, height=5)
    correct_msg.place(x=10,y=10)
    if happy == 1:
        correct_msg.insert(1.0, "Correct answer!")
    if anger == 2:
        correct_msg.insert(1.0, "Wow! Another correct answer!")
    if anger == 3:
        correct_msg.insert(1.0, "I didn't expect that you'd be so good at this!")
    C.update
    if question == 1:
        timer_sec_que.start()
    if question == 2:
        timer_thi_que.start()
    if question == 3:
        timer_fou_que.start()

def firstQuestion():
    global question
    question = 1
    accept_and_start_btn.destroy()
    firstquestion = Text(master, width=45, height=5)
    firstquestion.place(x=10,y=10)
    firstquestion.insert(1.0, 'Splendid! First question, then...\nA semla is a traditional sweet roll that for instance is made in Sweden. If eaten togetherwith warm milk, what is the Swedish word for it?')
    C.create_window(200,120,window=hetvägg)
    C.create_window(100,120,window=grötbulle)
    C.create_window(300,120,window=samke)
    C.update()

def secondQuestion():
    global question
    question = 2
    hetvägg.destroy()
    grötbulle.destroy()
    samke.destroy()
    secondquestion = Text(master, width=45,height=5)
    secondquestion.place(x=10,y=10)
    secondquestion.insert(1.0, 'Second question! In a 2010 study, people \nfound more mistakes when they marked essays \nwith a pen of what colour?')
    C.create_window(50,120,window=green)
    C.create_window(150,120,window=red)
    C.create_window(250,120,window=blue)
    C.create_window(350,120,window=magenta)
    C.update()

def thirdQuestion():
    global question
    question = 3
    green.destroy()
    red.destroy()
    blue.destroy()
    magenta.destroy()
    thirdquestion = Text(master, width=45,height=5)
    thirdquestion.place(x=10,y=10)
    thirdquestion.insert(1.0, 'Moving on to the third question! What \nprincess was traditionally called \nBadr al-Budur before Disney renamed her?')
    C.create_window(50,120,window=jasmine)
    C.create_window(150,120,window=ariel)
    C.create_window(250,120,window=anna)
    C.create_window(350,120,window=belle)
    C.update()

def fourthQuestion():
    global question
    question = 4
    jasmine.destroy()
    ariel.destroy()
    anna.destroy()
    belle.destroy()
    fourthquestion = Text(master, width=45,height=5)
    fourthquestion.place(x=10,y=10)
    fourthquestion.insert(1.0, '')

event = threading.Event()
timer_sec_que = threading.Timer(3, secondQuestion)
timer_thi_que = threading.Timer(3,thirdQuestion)
timer_fou_que = threading.Timer(5,fourthQuestion)

introtext = Text(master, width=45, height=5)
start_btn = Button(master, text='Start', command = begin)
accept_and_start_btn = Button (master, text='Okay', command = firstQuestion)
#FIRST QUESTION
hetvägg = Button(master, text='Hetvägg', command=correct) #CORRECT
grötbulle = Button (master, text = 'Grötbulle', command = incorrect) #INCORRECT
samke = Button(master, text = 'Samke', command = incorrect) #INCORRECT
#SECOND QUESTION
green = Button(master, text = 'Green', command = incorrect) #INCORRECT
blue = Button(master, text = 'Blue', command = incorrect) #INCORRECT
red = Button(master, text = 'Red', command = correct) #CORRECT
magenta = Button(master, text = 'Magenta', command = incorrect) #INCORRECT
#THIRD QUESTION
belle = Button(master, text = 'Belle', command = incorrect) #INCORRECT
anna = Button(master, text = 'Anna', command = incorrect) #INCORRECT
jasmine = Button(master, text = 'Jasmine', command = correct) #CORRECT
ariel = Button(master, text = 'Ariel', command = incorrect) #INCORRECT
#FOURTH QUESTION


interface()
a = C.create_window(200, 120, window=start_btn)
C.update()

master.mainloop()