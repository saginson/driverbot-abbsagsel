from tkinter import *
#Generate base window
master = Tk()
    #Canvas
C = Canvas(master, bg='grey',height=600,width=400)
C.pack()

def interface():
    # C.create_window(window=introtext)
    introtext.place(x=10, y=10)
    introtext.insert(1.0, 'Welcome to...\nThe Personal and Very Customized quiz-night!\nPress a button. Any button!')
    introtext.config(state=DISABLED)
    # print("it's working, ITS WORKING!")

introtext = Text(master, width=45, height=5)