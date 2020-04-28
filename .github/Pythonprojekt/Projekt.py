from tkinter import *
import time
from threading import Timer
import threading
import databas
import random
#Generate base window

#VARIABLES ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
master = Tk()
    #Canvas
C = Canvas(master, bg='grey',height=600,width=400)
C.pack()
dic = databas.dic #döper om min dictionary från databasen
happlist = databas.happy #döper om listan "happy" som hämtas från databasen
angrlist = databas.angry #samma som ovan, fast för "angry"
angrrlist = databas.angry_angry #samma som ovan
happrlist = databas.happy_angry # samma som ovan
n = 0 #variabeln som förklarar vilken fråga som ska presenteras (visas mer i funktionen create())
happy = 0 #hur många rätta svar användaren fått
angry = 0 #hur många felaktiga svar användaren fått
right = "" #Rätta svaret har den här variabeln, självklart finns inget rätt svar innan det har börjat
maxfråg = databas.frågor #Hur många frågor det finns totalt (första frågan har värdet 0)
angrsvar = databas.angrsvar #Hur många svar som finns i listan "angry", som ovan har första svaret värde 0
angrrsvar = databas.angrrsvar #Hur många svar som finns i listan "angry_angry", som ovan har första svaret värde 0
happrsvar = databas.happrsvar #Hur många svar som finns i listan "happy_angry", som ovan har första svaret värde 0

#CLASSES AND FUNCTIONS ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        self.Qst = Text(master, width=45, height=5) #öppnar textfönstret och döper det till "Qst"
        self.Righty = Text(master, width=20, height=2) #öppnar textfönstret för rätt svar som döps till "Righty"
        #STOPPADE EN QUIT-BTN HÄR MEN FUNKTIONEN LÄNKAD TILL command 'is not defined' TROTS ATT JAG TILL OCH MED STOPPADE DEN I KLASSEN MED print("helo") SOM ENDA KODRADEN INUTI
    def open(self, question):
        global right
        self.Qst.delete(1.0,END) #rensar textfönstret
        self.Righty.delete(1.0,END)
        kaputt() #tar bort alla knappar
        self.Qst.place(x=10,y=10) #placerar textfönstret
        self.Qst.insert(1.0,question["Q"])
        # print(maxfråg)
        x = 0 #x ökar med 1 varje gång, motsvarar knappens plats och kan resettas 
        letters = 0 #Motsvarar antal bokstäver i knappen
        space = 0
        righty_height = 0 #Y-värdet för rutan med rätt svar
        #asgdwajkdgaskjdasg
        for m, answer in enumerate(question["svar"]): #för varje svar i listan "svar" (som då får ett värde beroende på platsen)
            # question["template"][m]
            # print(question["template"][m])
            if question["template"][m] == 1: #variabeln m står för platsen i listan "template" som finns i min dictionary, programmet kollar då en plats i taget och kollar ifall det är en etta eller nolla
                b = Button(C, text=answer, command = createTrue)
                right = answer
            if question["template"][m] == 0: # 1 är rätt, 0 är fel
                b = Button(C, text=answer, command = createFalse) #exempelvis ifall objektet är 0, då skapas en knapp med svaret som är fel som leder till funktionen som hör till felaktiga svar
            space = 20+20*x+letters*6 #Space motsvarar platsen som alla knappar tar på en rad
            if space+len(answer) > 300: #Denna if-loop avgör ifall knappen är för stor för ena raden och gör i så fall en ny rad
                print('IT TOO BIG')
                righty_height += 1
                space = 20 #Då resettas space, fast till 20 för att den nya knappen på andra raden inte ska sättas längst ut utan istället 20 pixlar in
                x=0 #Resettas då den första knappen på rad två har plats ett och inte tre, fyra, fem eller vad det nu kan vara
                letters = 0 #Antal bokstäver resettas också då antalet från föregående rad annars är med
            # print(space)
            b.place(x=space,y=115+35*righty_height) #
            x+=1
            letters += len(answer)+2
            # print(letters)

        self.Righty.place(x=10,y=150+35*righty_height)
        print(right)
        C.update()

    def kill(self):
        self.Qst.destroy()
        self.Righty.destroy()
        C.update()

    def responseTrue(self):
        global happy
        global angry
        happy+=1
        # print("True!!")
        if angry <= 4: #Fram tills användaren får 4 fel kommer reaktionerna vara positiva
            qst.Qst.insert(1.0,happlist[happy-1])
        if angry == 4 and happy == 1:
            qst.Qst.insert(1.0,angrrlist[2]) #Då används den tredje raden i mitt dictionary "angry_angry"
        if angry > 4 and happy > 0:
            qst.Qst.insert(1.0,happrlist[random.randint(0,happrsvar)]) #I mitt dictionary happy_angry har jag reaktioner som då väljs randomly så fort användaren svarat fel mer än 4 gånger


        qst.Righty.insert(1.0,"Correct answer: \n"+right)
        C.update()
        time.sleep(2)
        if happy > 9 and happy < 12:
            time.sleep(3)
        if happy >=12 and happy < 24:
            time.sleep(5)
        if happy == 20:
            time.sleep(3)
        if happy == 24:
            time.sleep(8)

        create()

    def responseFalse(self):
        global angry
        global happy
        angry+=1
        # print("False!!")
        if angry < 4 and happy >= 0:
            qst.Qst.insert(1.0,angrlist[angry-1])
        if angry >= 4 and happy > 0:
            qst.Qst.insert(1.0,angrlist[random.randint(3,angrsvar)])

            
        if angry == 4 and happy == 0:
            qst.Qst.insert(1.0,angrrlist[0])
        if angry == 5 and happy == 0:
            qst.Qst.insert(1.0,angrrlist[1])
        if angry >=6 and happy == 0:
            qst.Qst.insert(1.0,angrrlist[random.randint(3,angrrsvar)]) #Ifall du aldrig svarar rätt kommer du få slumpvalt valda svar från listan "angry_angry", dock inte de första tre för att jag specifikt använder dem

        qst.Righty.insert(1.0,"Correct answer: \n"+right)
        C.update()
        time.sleep(2)
        if angry == 4 and happy == 0:
            time.sleep(2)
        create()

#VARIABLES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
qst = Question() #Gör koden mindre rörig


#STANDALONE FUNCTIONS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kaputt():
    for widget in C.winfo_children(): #För varje knapp som skapats:
            widget.destroy() #Förstör den

def happyCheck(happy,checkHappy,mess):
    if happy == checkHappy:
        qst.Qst.insert(1.0,mess)
def angryCheck(angry,checkAngry,mess):
    if angry == checkAngry:
        qst.Qst.insert(1.0,mess)
   
def create():
    global n
    global qst
    global happy
    global angry
    n += 1 #n används under för att kontrollera vilken fråga som ska startas. fråg1, fråg2, fråg3 etc.
    print(n)
    if n == 2:
        quitToStart() #Avslutar quizzen och återvänder tillbörjan
        
    else:
        qst.open(dic["fråg"+str(n)]) #dic["fråg"+str(n)] sätts in i "question" i funktionen open() i klassen Question
       

def createFalse():
    qst.Qst.delete(1.0,END)
    qst.responseFalse()
def createTrue():
    qst.Qst.delete(1.0,END)
    qst.responseTrue()

def quitToStart():
    global n
    global qst
    global happy
    global angry
    kaputt()
    qst.kill()
    C.update()
    # qst.kill()
    ejntro = Intro() 
    print("delete?")
    ejntro.intro()
    qst = Question()
    n = 0
    happy = 0
    angry = 0

#VARIABLES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ejntro = Intro() #nu kan jag nå min Intro-klass genom "ejntro" och ha "ejntro.intro()" istället för "Intro.intro()" så att programmet och jag inte blir förvirrad


 
#BEGINNING --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ejntro.intro()
# print(dic["fråg1"]["Q"])

master.mainloop()