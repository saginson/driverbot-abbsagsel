from tkinter import *
import time
from threading import Timer
import threading
import databas
import random
#Generate base window

#VARIABLES ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
master = Tk()
C = Canvas(master, bg='grey',height=600,width=400) #Fönstret är basen för hela interfacen
C.pack()
dic = databas.dic #Underlättar för mig då det blir mindre att skriva
happlist = databas.happy #Samma som ovan
angrlist = databas.angry #samma som ovan
angrrlist = databas.angry_angry #samma som ovan
happrlist = databas.happy_angry # samma som ovan
n = 0 #användningsområdet visas i funktionen create()
happy = 0 #fungerar som en räknare för hur många rätta svar användaren fått
angry = 0 # --II-- hur många felaktiga svar användaren fått
right = "" #variabelns värde är det nuvarande rätta svaret, för att lätt kunna få tag på det
maxfråg = databas.frågor #variabelns värde motsvarar hur många frågor det finns totalt
angrsvar = databas.angrsvar #variabelns värde motsvarar hur många svar som finns i listan "angry"
angrrsvar = databas.angrrsvar #variabelns värde motsvarar hur många svar som finns i listan "angry_angry"
happrsvar = databas.happrsvar #variabelns värde motsvarar hur många svar som finns i listan "happy_angry"
dev = databas.dev #Förkortningen underlättar för mig

#CLASSES AND FUNCTIONS ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Intro:
    def __init__(self):
        self.introtext = Text(C, width=45, height=5)
        self.start_btn = Button(C, text='Start', command = create)
        self.quit_game = Button(C, text='Terminate', command = quit)
        self.check_highscore = Button(C, text='Check Current High Score', width=22,command = toggleToggle)
        
    def intro(self):
        self.start_btn.place(x=50,y=110)
        self.quit_game.place(x=275, y=110)
        self.introtext.place(x=10, y=10)
        self.check_highscore.place(x=100, y=110)
        self.introtext.insert(1.0, "Welcome to...\nThe Personal and Very Customized quiz-night!\n*cheering* Press a button. Any button!\n")
        C.update() #Här uppdateras canvasen så att användaren ser förändringarna

    def toggle_text(self):
        global data #Jag gör många värden globala i funktioner då function parameters inte är kompatibla med tkinter
        if self.check_highscore["text"] == "Check Current High Score":
            self.check_highscore["text"] = "Current High Score: "+data
        else:
            self.check_highscore["text"] = "Check Current High Score"


class Question:
    def __init__(self):
        self.Qst = Text(master, width=45, height=5) #textfönstret där frågorna syns
        self.Righty = Text(master, width=20, height=2) #textfönstret med rätt svar
    def open(self, question):
        global right
        global clos
        clos = qst #Variabeln "clos" kan antingen vara qst eller end beroende på ifall användaren vill återgå till menyn från klassen Question eller Ending, används i funktionen "closeCurrent"
        self.Qst.delete(1.0,END) #rensar textfönstret för att texten annars inte kan ersättas
        self.Righty.delete(1.0,END)
        kaputt() #tar bort alla knappar så att de inte kolliderar med de nya som skapas
        self.i_want_out = Button(C, text='Quit', command = quitToStart) #Knappen för att avsluta och återgå till startmenyn
        self.i_want_out.place(x=340,y=10)
        self.Qst.place(x=10,y=40) #placerar textfönstret
        self.Qst.insert(1.0,question["Q"])
        x = 0 #x ökar med 1 varje gång, motsvarar knappens plats och kan resettas 
        letters = 0 #Motsvarar antal bokstäver i knappen
        space = 0
        righty_height = 0 #Y-värdet för rutan med rätt svar
        for m, answer in enumerate(question["svar"]): #för varje svar i listan "svar" (som då får ett värde beroende på platsen)
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
            b.place(x=space,y=135+35*righty_height) #
            x+=1
            letters += len(answer)+2

        self.Righty.place(x=10,y=170+35*righty_height)
        print(right)
        C.update()

    def kill(self):
        self.Qst.destroy()
        self.Righty.destroy()
        self.i_want_out.destroy()
        C.update()

    def responseTrue(self):
        global happy
        global angry
        happy+=1
        freeze()
        self.next_btn = Button(C, bg= 'green', text = 'Next', command = create)
        self.next_btn.place(x=300,y=10)
        if angry <= 4: #Fram tills användaren får 4 fel kommer reaktionerna vara positiva
            qst.Qst.insert(1.0,happlist[happy-1])
        if angry == 4 and happy == 1:
            qst.Qst.insert(1.0,angrrlist[2]) #Då används den tredje raden i mitt dictionary "angry_angry"
        if angry > 4 and happy > 0:
            qst.Qst.insert(1.0,happrlist[random.randint(0,happrsvar)]) #I mitt dictionary happy_angry har jag reaktioner som då väljs randomly så fort användaren svarat fel mer än 4 gånger


        qst.Righty.insert(1.0,"Correct answer: \n"+right)
        C.update()

    def responseFalse(self):
        global angry
        global happy
        angry+=1
        freeze()
        self.next_btn = Button(C, bg= 'green', text = 'Next', command = create)
        self.next_btn.place(x=300,y=10)
        if angry < 4 and happy >= 0:
            qst.Qst.insert(1.0,angrlist[angry-1]) #Så länge du inte svarat mer än fyra fel kommer du få de tre första raderna från listan "angry", därefter kommer den nedan
        if angry >= 4 and happy > 0:
            qst.Qst.insert(1.0,angrlist[random.randint(3,angrsvar)]) #Ifall du aldrig svarar rätt kommer du få slumpvalt valda svar från listan "angry", dock inte de första tre för att jag specifikt använder dem

        #SPECIFIKA SITUATIONER
        if angry == 4 and happy == 0: #Ifall du svarar fel den fjärde gången och aldrig svarat rätt
            qst.Qst.insert(1.0,angrrlist[0])
        if angry == 5 and happy == 0: #Ifall du svarar fel den femte gången och aldrig svarat rätt
            qst.Qst.insert(1.0,angrrlist[1])
        if angry >=6 and happy == 0: #Ifall du svarar fel den sjätte gången och aldrig svarat rätt
            qst.Qst.insert(1.0,angrrlist[random.randint(3,angrrsvar)]) #Ifall du aldrig svarar rätt kommer du få slumpvalt valda svar från listan "angry_angry", dock inte de första tre för att jag specifikt använder dem

        qst.Righty.insert(1.0,"Correct answer: \n"+right) #Skriver in det korrekta svaret i textrutan under knapparna, som heter "Righty"
        C.update()

class Ending:
    def __init__(self):
        self.Results = Text(master, width=45, height=15)
    def showcase(self):
        global happy
        global angry
        global clos
        global score
        global data
        readHighScore()
        clos = end
        score = (happy-angry+24)*20
        print("score: "+str(score))
        self.i_want_out = Button(C, text='Return to Menu', command = quitToStart) #Knappen för att avsluta och återgå till startmenyn
        self.high_score = Button(C, text='Save as High Score', command = saveHighScore)
        self.reset_high_score = Button(C, text='Reset High Score', command = resetHighScore)
        self.i_want_out.place(x=280,y=260)
        self.high_score.place(x=150,y=260)
        self.reset_high_score.place(x=30, y=260)
        self.Results.place(x=10, y=10)
        self.Results.insert(1.0,"Your final score: "+str(score)+"\nCurrent high score: "+data+"\n------------------\nCorrect answers: "+str(happy)+"\nIncorrect answers: "+str(angry)+"\n------------------\nComment from developer: \n"+dev[happy])
        C.update()

    def kill(self):
        self.Results.destroy()
        self.i_want_out.destroy()


#VARIABLES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
qst = Question() #Gör koden mindre rörig och underlättar att nå funktioner innanför klasserna
end = Ending()

#STANDALONE FUNCTIONS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kaputt():
    for widget in C.winfo_children(): #För varje knapp som skapats:
        widget.destroy() #Förstör den
def freeze():
    for widget in C.winfo_children():
        widget.config(state=DISABLED)
   

def create():
    global n
    global qst
    global happy
    global angry
    n += 1 #n används under för att kontrollera vilken fråga som ska startas. fråg1, fråg2, fråg3 etc. i mitt else-påstående längre ned
    print(n)
    if n == 24: #IFALL DU VILL PROVA SLUTFUNKTIONEN UTAN ATT GENOMLIDA DEN LÅNGA PROCESSEN, ÄNDRA "n == 24" TILL "n == 2"
        endOfGame() #Kallar på funktionen som visar ditt resultat
    else:
        qst.open(dic["fråg"+str(n)]) #dic["fråg"+str(n)] sätts in i "question" i funktionen open() i klassen Question
       

def createFalse():
    qst.Qst.delete(1.0,END) #Rensar textrutan
    qst.responseFalse() #Funktionen som skriver ut text kopplad till ett inkorrekt svar
def createTrue():
    qst.Qst.delete(1.0,END) #Rensar textrutan
    qst.responseTrue() #Funktionen som skriver ut text kopplad till ett korrekt svar

def quitToStart():
    global happy
    global angry
    closeCurrent() #Jag använder funktionen för att slippa ha dess inehåll i både quitToStart och endOfGame
    C.update() #Uppdaterar canvasen
    ejntro.intro() #Startmenyn öppnas
    happy = 0 #Resettar korrekta och inkorrekta svar här då de behövs för att beräkna ditt slutresultat i endOfGame och kan inte vara i closeCurrent
    angry = 0
def endOfGame():
    closeCurrent()
    C.update() #Uppdaterar canvasen
    end.showcase() #Visar ditt score, antal rätt/fel svar och en kommentar från mig


def closeCurrent():
    global n
    global qst
    global end
    global clos
    global ejntro
    kaputt() #Tar bort all knappar som varit svaren och "quit"
    clos.kill() #Tar bort alla textfönster och knappar som varit "permanenta" inom klassen tidigare (de som inte tas bort varje gång en ny fråga dyker upp)
    C.update() #Uppdaterar canvasen
    ejntro = Intro() #Ifall att klassen ska öppnas igen kommer __init__ att köras så att allt skapas igen, samma sak med "qst = Question()" samt "end = Ending()"
    qst = Question()
    end = Ending() 
    n = 0 #Resettar värdet ändras när du svarar på frågor (då rundan är klar)


def saveHighScore():
    global score
    with open ("C:/Users/Sagis/Documents/GitHub/driverbot-abbsagsel/.github/Pythonprojekt/save.txt", "w") as fil:
        fil.write(str(score))

def resetHighScore():
    global end
    with open ("C:/Users/Sagis/Documents/GitHub/driverbot-abbsagsel/.github/Pythonprojekt/save.txt", "w") as fil:
        fil.write(str(0))

def readHighScore():
    global data
    with open ("C:/Users/Sagis/Documents/GitHub/driverbot-abbsagsel/.github/Pythonprojekt/save.txt") as fil:
        data = fil.read()

def toggleToggle():
    readHighScore()
    ejntro.toggle_text()
    

#VARIABLES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ejntro = Intro() #nu kan jag nå min Intro-klass genom "ejntro" och ha "ejntro.intro()" istället för "Intro.intro()" så att programmet och jag inte blir förvirrad


 
#BEGINNING --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ejntro.intro()
# print(dic["fråg1"]["Q"])

master.mainloop()