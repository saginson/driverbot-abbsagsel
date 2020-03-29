from tkinter import *
import time
from threading import Timer
import threading
import databas
#Generate base window

#VARIABLES
master = Tk()
    #Canvas
C = Canvas(master, bg='grey',height=600,width=400)
C.pack()
dic = databas.dic
happlist = databas.happy
angrlist = databas.angry
n = 0 #variabeln som förklarar vilken fråga som ska presenteras (visar längre ner i funktionen open() i class Question)
happy = 0
angry = 0


class Intro:
    def __init__(self):
        self.introtext = Text(C, width=45, height=5)
        self.start_btn = Button(C, text='Start', command = create)
        
    def intro(self):
        # C.create_window(100, 120, window=self.start_btn)
        self.start_btn.place(x=100,y=110)
        self.introtext.place(x=10, y=10)
        self.introtext.insert(1.0, 'Welcome to...\nThe Personal and Very Customized quiz-night!\n*cheering* Press a button. Any button!')
        C.update()

class Question:
    def __init__(self):
        self.Qst = Text(master, width=45, height=5)

    def open(self, question):
        #HÄR STARTAR FRÅGORNA
        self.Qst.delete(1.0,END)
        kaputt()
        print("?")
        self.Qst.place(x=10,y=10)
        self.Qst.insert(1.0,question["Q"]) #här används n för att kontrollera ifall det ska vara fråg1, fråg2 eller fråg3 som ska visas. fråg1, fråg2 och fråg3 finns i filen databas som jag importerar
        print(question["Q"])
        m = 0
        for answer in question["svar"]:
            question["template"][m]
            print(question["template"][m])
            if question["template"][m] == 1:
                b = Button(C, text=answer, command = createTrue)
            if question["template"][m] == 0:
                b = Button(C, text=answer, command = createFalse)
            b.place(x=20+m*85,y=110)
            m+=1
        
        C.update()

    def responseTrue(self):
        global happy
        global angry
        happy+=1
        print("True!!")
        if angry < 4:
            qst.Qst.insert(1.0,happlist[happy-1])

        C.update()
        time.sleep(2)
        create()

    def responseFalse(self):
        global angry
        global happy
        angry+=1
        print("False!!")
        if angry < 4:
            qst.Qst.insert(1.0,angrlist[angry-1])

        C.update()
        time.sleep(2)
        create()





#VARIABLES
qst = Question()


#CODE
def kaputt():
    for widget in C.winfo_children():
            widget.destroy()
def happyCheck(happy,checkHappy,mess):
    if happy == checkHappy:
        qst.Qst.insert(1.0,mess)
def angryCheck(angry,checkAngry,mess):
    if angry == checkAngry:
        qst.Qst.insert(1.0,mess)

    
def create():
    global n
    n += 1
    qst.open(dic["fråg"+str(n)])
def createFalse():
    qst.Qst.delete(1.0,END)
    qst.responseFalse()
def createTrue():
    qst.Qst.delete(1.0,END)
    qst.responseTrue()


#VARIABLES
ejntro = Intro() #nu kan jag nå min Intro-klass och ha "ejntro.intro()" istället för "Intro.intro()" så att programmet och jag inte blir förvirrad


#BEGINNING
ejntro.intro()
# print(dic["fråg1"]["Q"])

master.mainloop()