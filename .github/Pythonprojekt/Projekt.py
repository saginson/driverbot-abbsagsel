from tkinter import *
import time
from threading import Timer
import threading
import databas
import random
import os

#VARIABLER ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
master = Tk()
C = Canvas(master, bg='grey',height=600,width=400) #fönstret är basen för hela interfacen
C.pack()
dic = databas.dic #koden ser mindre rörig ut
happlist = databas.happy #samma som ovan
angrlist = databas.angry #samma som ovan
angrrlist = databas.angry_angry #samma som ovan
happrlist = databas.happy_angry # samma som ovan
n = 0 #vilken fråga som ska köras, användningsområdet för n visas i funktionen create()
happy = 0 #fungerar som en räknare för hur många rätta svar användaren fått
angry = 0 # ---II--- felaktiga svar användaren fått
right = "" #variabelns värde är det nuvarande rätta svaret, för att lätt kunna få tag på det
maxfråg = databas.frågor #motsvarar hur många frågor det finns totalt
angrsvar = databas.angrsvar #motsvarar hur många svar som finns i listan "angry"
angrrsvar = databas.angrrsvar #motsvarar hur många svar som finns i listan "angry_angry"
happrsvar = databas.happrsvar # motsvarar hur många svar som finns i listan "happy_angry"
#KLASSER AND FUNKTIONER -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Intro:
    def __init__(self):
        self.introtext = Text(C, width=45, height=5) #här läggs textrutan i canvasen,(C, ...) istället för i master, och är därför mer flexibel och kan tex. tas bort
        self.start_btn = Button(C, text='Start', command = create) #det viktiga att veta här är att "command" kopplar knappen till en funktion
        self.quit_game = Button(C, text='Terminate', command = quit)
        self.check_highscore = Button(C, text='Check Current High Score', width=22, command = toggleToggle)
        
    def intro(self):
        self.start_btn.place(x=50,y=110) #x och y-värden anges för att placera komponenten
        self.quit_game.place(x=275, y=110)
        self.introtext.place(x=10, y=10)
        self.check_highscore.place(x=100, y=110)
        self.introtext.insert(1.0, "Welcome to...\nThe Personal and Very Customized quiz-night!\n*cheering* Press a button. Any button!\n")
        C.update() #här uppdateras canvasen så att användaren ser förändringarna

    def toggle_text(self): #funktionen används för att visa det aktuella rekordet och möjliggörs genom funktionen toggleToggle
        global data #jag gör många värden globala i funktioner då function parameters inte är kompatibla med tkinter
        if self.check_highscore["text"] == "Check Current High Score":
            self.check_highscore["text"] = "Current High Score: "+data #data motsvarar det aktuella rekordet
        else:
            self.check_highscore["text"] = "Check Current High Score"


class Question:
    def __init__(self):
        self.Qst = Text(master, width=45, height=5) #textfönstret där frågorna syns
        self.Righty = Text(master, width=20, height=2) #textfönstret med rätt svar
    def open(self, question):
        global right
        global clos
        clos = qst #uppger vilken klass användaren befinner sig i, används i funktionen "closeCurrent" för att rensa komponenter
        self.Qst.delete(1.0,END) #rensar textfönstret för att texten annars inte kan ersättas
        self.Righty.delete(1.0,END)
        kaputt() #tar bort alla knappar så att de inte kolliderar med de nya som skapas
        self.i_want_out = Button(C, text='Quit', command = quitToStart) #använder funktionen quitToStart
        self.i_want_out.place(x=340,y=10)
        self.Qst.place(x=10,y=40)
        self.Qst.insert(1.0,question["Q"])
        x = 0 #x ökar med 1 varje gång, motsvarar knappens plats i den nedre loopen och kan resettas 
        letters = 0 #motsvarar antal bokstäver som finns i knappen i nedre loopen
        space = 0 #space motsvarar platsen som alla knappar tar på en rad
        righty_height = 0 #y-värdet för rutan med rätt svar
        for m, answer in enumerate(question["svar"]): #för varje svar i listan "svar" (som då får ett värde beroende på platsen) genom variabeln answer får jag även själva svaret
            if question["template"][m] == 1: #variabeln m står för svarets plats i listan och programmet kollar ifall motsvarande plats i listan "template" innehåller 1 eller 0
                b = Button(C, text=answer, command = createTrue) #funktionen createTrue körs ifall användaren trycker på knappen
                right = answer
            if question["template"][m] == 0:
                b = Button(C, text=answer, command = createFalse) #funktionen createFalse körs ifall användaren trycker på knappen
            space = 20+20*x+letters*6 # ett förhållande som ger ett lagom mellanrum mellan knapparna
            if space+len(answer) > 300: #denna if-loop avgör ifall knappen är för stor för ena raden och gör i så fall en ny rad
                righty_height += 1 #kommer flytta textrutan med rätt svar en rad ner
                space = 20 #space resettas till 20 för att den nya knappen på andra raden inte ska sättas längst ut utan istället 20 pixlar in
                x=0 #resettas då den första knappen på rad två har plats ett
                letters = 0 #antal bokstäver resettas då antalet från föregående rad annars är med
            b.place(x=space,y=135+35*righty_height) #placeringen av knappen
            x+=1
            letters += len(answer)+2

        self.Righty.place(x=10,y=170+35*righty_height) #placeringen av textrutan med rätt svar
        C.update()

    def kill(self): #tar bort komponenterna som finns i master (master, ...)
        self.Qst.destroy()
        self.Righty.destroy()
        C.update()

    def responseTrue(self): #genererar en reaktion på rätt svar
        global happy
        global angry
        happy+=1
        freeze() #hindrar användaren från att trycka på knapparna mer än en gång när reaktionen visas
        self.next_btn = Button(C, bg= 'green', text = 'Next', command = create) #knappen för att fortsätta med nästa fråga
        self.next_btn.place(x=300,y=10)
        if angry <= 4: #fram tills användaren får 4 fel kommer reaktionerna komma från listan "happy"
            qst.Qst.insert(1.0,happlist[happy-1])
        if angry == 4 and happy == 1:
            qst.Qst.insert(1.0,angrrlist[2])
        if angry > 4 and happy > 0:
            qst.Qst.insert(1.0,happrlist[random.randint(0,happrsvar)]) #i listan happy_angry finns strings som väljs slumpmässigt så fort användaren svarat fel mer än 4 gånger

        qst.Righty.insert(1.0,"Correct answer: \n"+right) #skriver ut rätt svar
        C.update()

    def responseFalse(self): #genererar en reaktion på fel svar
        global angry
        global happy
        angry+=1
        freeze()
        self.next_btn = Button(C, bg= 'green', text = 'Next', command = create)
        self.next_btn.place(x=300,y=10)
        if angry < 4 and happy >= 0:
            qst.Qst.insert(1.0,angrlist[angry-1]) #så länge du inte svarat mer än 4 fel kommer du få de tre första raderna från listan "angry", därefter kommer den nedan
        if angry >= 4 and happy > 0:
            qst.Qst.insert(1.0,angrlist[random.randint(3,angrsvar)]) #användaren visas slumpmässigt valda strings från listan "angry"

        #SPECIFIKA SITUATIONER
        if angry == 4 and happy == 0:
            qst.Qst.insert(1.0,angrrlist[0])
        if angry == 5 and happy == 0:
            qst.Qst.insert(1.0,angrrlist[1])
        if angry >=6 and happy == 0:
            qst.Qst.insert(1.0,angrrlist[random.randint(3,angrrsvar)]) #ifall användaren aldrig svarar rätt kommer slumpmässigt valda strings från listan "angry_angry" visas

        qst.Righty.insert(1.0,"Correct answer: \n"+right) #skriver ut rätt svar
        C.update()

class Ending:
    def __init__(self):
        self.Results = Text(master, width=45, height=15) #textrutan som syns på slutet
    def showcase(self):
        global happy
        global angry
        global clos
        global score
        global data
        readHighScore() #data har värdet av rekordet
        clos = end
        score = (happy-angry+24)*20 #slutpoängen
        self.i_want_out = Button(C, text='Return to Menu', command = quitToStart)
        self.high_score = Button(C, text='Save as High Score', command = saveHighScore)
        self.reset_high_score = Button(C, text='Reset High Score', command = resetHighScore)
        self.i_want_out.place(x=280,y=260)
        self.high_score.place(x=150,y=260)
        self.reset_high_score.place(x=30, y=260)
        self.Results.place(x=10, y=10)
        self.Results.insert(1.0,"Your final score: "+str(score)+"\nCurrent high score: "+data+"\n------------------\nCorrect answers: "+str(happy)+"\nIncorrect answers: "+str(angry)+"\n------------------\nComment from developer: \n"+databas.dev[happy])
        C.update()

    def kill(self): #tar bort komponenter som finns i master
        self.Results.destroy()

#VARIABLER --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
qst = Question() #gör koden mindre rörig och underlättar att nå funktioner som finns i klasserna
end = Ending()
#STANDALONE-FUNKTIONER --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kaputt(): #tar bort komponenter som finns i canvas (C, ...)
    for widget in C.winfo_children():
        widget.destroy()
def freeze(): #fryser komponenter som finns i canvas
    for widget in C.winfo_children():
        widget.config(state=DISABLED)

def create(): #sätter igång nästa fråga
    global n
    global qst
    global happy
    global angry
    n += 1 #n används under för att kontrollera vilken fråga som ska startas. fråg1, fråg2, fråg3 etc. i else-påståendet längre ned
    if n == 25: #IFALL DU VILL PROVA SLUTFUNKTIONEN UTAN ATT GENOMLIDA DEN LÅNGA PROCESSEN, ÄNDRA "n == 25" TILL "n == 2"
        endOfGame()
    else:
        qst.open(dic["fråg"+str(n)]) #dic["fråg"+str(n)] får variabeln "question" i funktionen open() för att ge mindre rörig kod
       
def createFalse(): #skickar till funktionen responseFalse()
    qst.Qst.delete(1.0,END)
    qst.responseFalse()
def createTrue(): #skickar till funktionen responseTrue()
    qst.Qst.delete(1.0,END)
    qst.responseTrue()

def quitToStart(): #avslutar mitt i
    global happy
    global angry
    closeCurrent()
    C.update() #uppdaterar canvasen
    ejntro.intro() #startmenyn öppnas
    happy = 0 #resettar korrekta och inkorrekta svar här då de behövs för att beräkna ditt slutresultat i endOfGame och kan inte vara i closeCurrent
    angry = 0
def endOfGame(): #spelet är slut
    closeCurrent()
    C.update() #uppdaterar canvasen
    end.showcase() #visar ditt score, antal rätt/fel svar och en kommentar från mig

def closeCurrent(): #rensar och städar fönstret
    global n
    global qst
    global end
    global clos
    global ejntro
    kaputt() #tar bort all knappar som finns i canvasen
    clos.kill() #tar bort alla textfönster och knappar som varit "permanenta" inom klassen tidigare (de som inte tas bort varje gång en ny fråga dyker upp)
    C.update() #uppdaterar canvasen
    ejntro = Intro() #ifall att klassen ska öppnas igen kommer __init__ att köras så att allt skapas igen, samma sak med "qst = Question()" samt "end = Ending()"
    qst = Question()
    end = Ending() 
    n = 0 #resettar värdet ändras när du svarar på frågor (då rundan är klar)

def saveHighScore():
    global score
    with open (os.getcwd() +"\\.github\\Pythonprojekt\\save.txt", "w") as fil: 
        fil.write(str(score))

def resetHighScore():
    global end
    with open (os.getcwd() +"\\.github\\Pythonprojekt\\save.txt", "w") as fil:
        fil.write(str(0))

def readHighScore():
    global data
    with open (os.getcwd() +"\\.github\\Pythonprojekt\\save.txt") as fil:
        data = fil.read()

def toggleToggle():
    readHighScore()
    ejntro.toggle_text()
    
#VARIABLER --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ejntro = Intro() #förebygger förvirring då funktionen intro i klassen intro annars nås genom intro.intro
#BÖRJAN -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ejntro.intro()

master.mainloop()