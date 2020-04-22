# from tkinter import *
# import time
# from threading import Timer
# import threading
# #Generate base window
# master = Tk()
#     #Canvas
# C = Canvas(master, bg='grey',height=600,width=400)
# C.pack()

# anger = 0
# happy = 0
# question = 0
# introduction = False

# sentences = [
#     "How are you today?",
#     "Ok.",
#     "Have you learned anything yet?"
# ]
# class Intro:
#     def __init__(self):
#         self.introtext = Text(master, width=45, height=5)
#         self.start_btn = Button(master, text='Start', command = firstQuestion)
#         self.info = info
#         self.extra = extra
        
        
#     def create(self):
#         self.introtext.place(x=10, y=10)
#         self.introtext.insert(1.0, 'Welcome to...\nThe Personal and Very Customized quiz-night!\n*cheering* Press a button. Any button!')
#         self.introtext.config(state=DISABLED)
#         C.create_window(100, 120, window=self.start_btn)
#         C.create_window(200, 120, window=info)
#         C.create_window(300, 120, window=extra)

#     def interface(self):
#         global infotext
#         global introduction
#         if introduction == True:
#             infotext.destroy()
#             goback_btn.destroy()
#             introduction = False
#         # C.create_window(window=introtext)

# def extra():
#     print("extra")
#     C.create_window(200,200,window=smalltalk)

# def smallTalk():
#     print("small talk")

# def infoText():
#     global infotext
#     global introduction
#     infotext = Text(master, width=45, height=10)
#     infotext.place(x=10,y=10)
#     infotext.insert(1.0, 'What I want you to do is... To answer every \nquestion honestly. \nI dont want to see you pressing any "random \nbuttons", got it?\nAlso! The correct answer will be displayed atthe bottom of this screen and not disappear \nuntil you have answered another question \nincorrectly! Take your time and if you find \nsomething interesting to read, remember that.')
#     infotext.config(state=DISABLED)
#     C.create_window(200,200,window=goback_btn)
#     introduction = True
# def incorrect():
#     rightAnswer()
#     global anger
#     global question
#     anger=anger +1 #räknar hur många gånger du svarat fel
#     incorrect_msg = Text(master, width=45, height=5)
#     incorrect_msg.place(x=10,y=10)
#     if anger == 1:
#         incorrect_msg.insert(1.0, "Oh no. You didn't actually know the answer?")
#     if anger == 2:
#         incorrect_msg.insert(1.0, "Another answer you didn't know, huh?")
#     if anger == 3:
#         incorrect_msg.insert(1.0, "OF COURSE you didn't know the answer! Why do I even bother with you?")
#     if anger == 4 and happy == 0:
#         incorrect_msg.insert(1.0, "WHY CAN'T YOU JUST BE SMART LIKE YOUR \nSIBLINGS?! *cough* *cough* You know what? \nFine. The right answer to the next question \nis number three. Mexico. Número tres.")
#     if anger == 4 and happy > 0:
#         incorrect_msg.insert(1.0, "WHY CAN'T YOU JUST BE SMART LIKE YOUR \nSIBLINGS?! *cough* *cough* It's fine. I'm \nFINE.")
#     if anger == 5 and happy == 0:
#         incorrect_msg.insert(1.0, "WHY WON'T YOU LISTEN TO ME, YOU LITTLE \nSHIT?! I TOLD YOU MEXICO WAS THE RIGHT \nANSWER!!!")
#     if anger == 5 and happy > 0:
#         incorrect_msg.insert(1.0, "*Heavy breathing*")
#     if anger == 6 and happy > 0:
#         incorrect_msg.insert(1.0, "I don't know... Is this even worthwhile? I mean, you aren't learning anything.")
#     if anger == 6 and happy == 0:
#         incorrect_msg.insert(1.0, "You are SUCH a dumb, mean person! *cries* \nI don't wanna do this anymore!")

#     incorrect_msg.config(state=DISABLED)
#     C.update
#     if question == 1:
#         timer_sec_que.start()
#     if question == 2:
#         timer_thi_que.start()
#     if question == 3:
#         timer_fou_que.start()
#     if question == 4:
#         timer_fiv_que.start()
#     if question == 5:
#         timer_six_que.start()


# def correct():
#     global happy
#     global question
#     global anger
#     happy = happy +1  #räknar hur många gånger du svarat rätt
#     correct_msg = Text(master, width=45, height=5)
#     correct_msg.place(x=10,y=10)
#     if happy == 1 and anger == 0:
#         correct_msg.insert(1.0, "Correct answer!")
#     if happy == 2:
#         correct_msg.insert(1.0, "Wow! Another correct answer!")
#     if happy == 3:
#         correct_msg.insert(1.0, "I didn't expect that you'd be so good at this!")
#     if happy == 4:
#         correct_msg.insert(1.0, "Correct! How admirable! *swoons*")
#     if anger == 4 and happy == 1:
#         correct_msg.insert(1.0, "Correct! See? I told you so")
#     if anger > 4:
#         correct_msg.insert(1.0, "Correct. You think you're good? Nah, that's \njust luck.")
#     if happy == 5 and anger <= 4:
#         correct_msg.insert(1.0, "Oh mah God! CAN I ADOPT YOU?!")
#     if happy == 6 and anger <= 4:
#         correct_msg.insert(1.0, "You must be a MASTERMIND! *applause*")
#     if happy == 6 and anger > 4:
#         correct_msg.insert(1.0, "Yeah. Lucky again, I see...")

#     correct_msg.config(state=DISABLED)
#     C.update
#     if question == 1:
#         timer_sec_que.start()
#     if question == 2:
#         timer_thi_que.start()
#     if question == 3:
#         timer_fou_que.start()
#     if question == 4:
#         timer_fiv_que.start()
#     if question == 5:
#         timer_six_que.start()

# def rightAnswer():
#     global question
#     rightanswer = Text(master, width=20, height=3)
#     rightanswer.place(x=10,y=200)
#     if question == 1:
#         msg = "Hetvägg"
#     if question == 2:
#         msg = "Red"
#     if question == 3:
#         msg = "Jasmine"
#     if question == 4:
#         msg = "Wings"
#     if question == 5:
#         msg = "Mexico"
#     if question == 6:
#         msg = "FALSE! It's actually native to China"
#     rightanswer.insert(1.0, "Right answer: \n"+msg+"!")
#     rightanswer.config(state=DISABLED)

# def firstQuestion(introtext, start_btn):
#     global question
#     global info
#     global extra
#     question = 1
#     introtext.destroy()
#     self.start_btn.destroy()
#     info.destroy()
#     extra.destroy()
#     firstquestion = Text(master, width=45, height=5)
#     firstquestion.place(x=10,y=10)
#     firstquestion.insert(1.0, 'Splendid! First question, then...\nA semla is a traditional sweet roll that for instance is made in Sweden. If eaten togetherwith warm milk, what is the Swedish word for it?')
#     C.create_window(200,120,window=hetvägg)
#     C.create_window(100,120,window=grötbulle)
#     C.create_window(300,120,window=samke)
#     firstquestion.config(state=DISABLED)
#     C.update()

# def secondQuestion():
#     global question
#     question = 2
#     hetvägg.destroy()
#     grötbulle.destroy()
#     samke.destroy()
#     secondquestion = Text(master, width=45,height=5)
#     secondquestion.place(x=10,y=10)
#     secondquestion.insert(1.0, 'Second question! In a 2010 study, people \nfound more mistakes when they marked essays \nwith a pen of what colour?')
#     C.create_window(50,120,window=green)
#     C.create_window(150,120,window=red)
#     C.create_window(250,120,window=blue)
#     C.create_window(350,120,window=magenta)
#     secondquestion.config(state=DISABLED)
#     C.update()

# def thirdQuestion():
#     global question
#     question = 3
#     green.destroy()
#     red.destroy()
#     blue.destroy()
#     magenta.destroy()
#     thirdquestion = Text(master, width=45,height=5)
#     thirdquestion.place(x=10,y=10)
#     thirdquestion.insert(1.0, 'Moving on to the third question! What \nprincess was traditionally called \nBadr al-Budur before Disney renamed her?')
#     C.create_window(50,120,window=jasmine)
#     C.create_window(150,120,window=ariel)
#     C.create_window(250,120,window=anna)
#     C.create_window(350,120,window=belle)
#     thirdquestion.config(state=DISABLED)
#     C.update()

# def fourthQuestion():
#     global question
#     question = 4
#     jasmine.destroy()
#     ariel.destroy()
#     anna.destroy()
#     belle.destroy()
#     fourthquestion = Text(master, width=45,height=5)
#     fourthquestion.place(x=10,y=10)
#     fourthquestion.insert(1.0, 'Do you like the Swedish questions? In \nSwedish, a skvader is a rabbit with what \nunusual feature?')
#     C.create_window(50,120,window=wings)
#     C.create_window(150,120,window=glasses)
#     C.create_window(250,120,window=no_ears)
#     C.create_window(350,120,window=giant_feet)
#     fourthquestion.config(state=DISABLED)
#     C.update()

# def fifthQuestion():
#     global question
#     question = 5
#     wings.destroy()
#     glasses.destroy()
#     no_ears.destroy()
#     giant_feet.destroy()
#     fifthquestion = Text(master, width=45,height=5)
#     fifthquestion.place(x=10,y=10)
#     fifthquestion.insert(1.0, 'More countries! Which country’s flag featuresan eagle eating a snake?')
#     C.create_window(50,120,window=mozambique)
#     C.create_window(150,120,window=dominica)
#     C.create_window(250,120,window=mexico)
#     C.create_window(350,120,window=guam)
#     fifthquestion.config(state=DISABLED)
#     C.update()

# def sixthQuestion():
#     global question
#     question = 6
#     mozambique.destroy()
#     dominica.destroy()
#     mexico.destroy()
#     guam.destroy()
#     sixthquestion = Text(master, width=45,height=5)
#     sixthquestion.place(x=10,y=10)
#     sixthquestion.insert(1.0, "Let's do a little TRUE or FALSE!\nThe kiwi fruit is native to New Zealand. True or false?")
#     C.create_window(150,120,window=kiwi_true)
#     C.create_window(250,120,window=kiwi_false)
#     sixthquestion.config(state=DISABLED)
#     C.update()

# def seventhQuestion():
#     global question
#     question = 7

# intro = Intro()
# event = threading.Event()

# timer_sec_que = threading.Timer(3, secondQuestion)
# timer_thi_que = threading.Timer(3,thirdQuestion)
# timer_fou_que = threading.Timer(5,fourthQuestion)
# timer_fiv_que = threading.Timer(8,fifthQuestion)
# timer_six_que = threading.Timer(8,sixthQuestion)
# timer_sev_que = threading.Timer(8,seventhQuestion)



# info = Button(master, text='Help', command = infoText)
# extra = Button(master, text='Extra', command = extra) #extra skulle kunna vara en klass
# smalltalk = Button(master, text='Small talk',command = smallTalk)
# goback_btn = Button(master, text ='Go Back', command = intro.interface)
# #FIRST QUESTION
# hetvägg = Button(master, text='Hetvägg', command=correct) #CORRECT
# grötbulle = Button (master, text = 'Grötbulle', command = incorrect) #INCORRECT
# samke = Button(master, text = 'Samke', command = incorrect) #INCORRECT
# #SECOND QUESTION
# green = Button(master, text = 'Green', command = incorrect) #INCORRECT
# blue = Button(master, text = 'Blue', command = incorrect) #INCORRECT
# red = Button(master, text = 'Red', command = correct) #CORRECT
# magenta = Button(master, text = 'Magenta', command = incorrect) #INCORRECT
# #THIRD QUESTION
# belle = Button(master, text = 'Belle', command = incorrect) #INCORRECT
# anna = Button(master, text = 'Anna', command = incorrect) #INCORRECT
# jasmine = Button(master, text = 'Jasmine', command = correct) #CORRECT
# ariel = Button(master, text = 'Ariel', command = incorrect) #INCORRECT
# #FOURTH QUESTION
# wings = Button(master, text = 'Wings', command = correct) #CORRECT
# glasses = Button(master, text = 'Glasses', command = incorrect) #INCORRECT
# no_ears = Button(master, text = 'No ears', command = incorrect) #INCORRECT
# giant_feet = Button(master, text = 'Giant feet', command = incorrect) #INCORRECT
# #FIFTH QUESTION
# dominica = Button(master, text = 'Dominica', command = incorrect) #INCORRECT
# mozambique = Button(master, text = 'Mozambique', command = incorrect) #INCORRECT
# guam = Button(master, text = 'Guam', command = incorrect) #INCORRECT
# mexico = Button(master, text = 'Mexico', command = correct) #CORRECT
# #SIXTH QUESTION
# kiwi_true = Button(master, text = 'TRUE', command = incorrect) #INCORRECT
# kiwi_false = Button(master, text = 'FALSE', command = correct) #CORRECT

# intro.create() 
# C.update()

# master.mainloop()