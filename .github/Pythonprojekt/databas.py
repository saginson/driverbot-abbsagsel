
angry = [
    "Oh no. You didn't actually know the answer?",
    "Another answer you didn't know, huh?",
    "OF COURSE you didn't know the answer! Why do I even bother with you?",
    "WHY CAN'T YOU JUST BE SMART LIKE YOUR \nSIBLINGS?! *cough* *cough* It's fine. I'm \nFINE.",
    "*Heavy breathing*",
    "I don't know... Is this even worthwhile? I mean, you clearly aren't learning anything.",
    "I knew you'd get this one wrong.",
    "You're having so much fun with this, \naren't you?",
    "Well, this is depressing."
    
]
angry_angry = [
    "WHY CAN'T YOU JUST BE SMART LIKE YOUR \nSIBLINGS?! *cough* *cough* You know what? \nFine. The right answer to the next question \nis number three. Mexico. Número tres.",
    "LISTEN HERE, YOU LITTLE SHIT! DON'T \nJUST IGNORE MY ADVICE LIKE THAT!!",
    "I told you. At least you got something\n right...",
    "You're worthless.",
    "Wrong answer. Expected? YES INDEED!",
    "I sense a deep frustration inside \nyou... or is it just me? I'm not sure...",
    "Oh I'm so disappointed..."
]
happy = [
    "Correct answer!",
    "Wow! Another correct answer!",
    "I didn't expect that you'd be so \ngood at this!",
    "Correct! How admirable! *swoons*",
    "Oh mah God! CAN I ADOPT YOU?!",
    "You must be a MASTERMIND! *applause*",
    "Honestly, I think the only right \ndecision would be to change positions...",
    "Why are you better than me at my job? \n*sobs* So unfair...",
    "How can you keep this much information \nin your head?",
    "I told my mom about you and she \ndoesn't believe that you're real.",
    "Am I sure that you're even human? \nThis is just so unbelievable...",
    "Oh? You're asking me what this is? \n Well, this is embarassing... I wrote a book \nabout you! It's gotten a bit of attention, \nactually.",
    "People have begged me to be introduced \nto you. They see you as some sort of God, \nor something... I don't know.",
    "I've put up an altar outside my house. \n What? I'm only doing it to keep the \npeople at bay, you know?",
    "They... They tried breaking into my \nhouse. With no success, of course.",
    "I'm starting to doubt that this is \ngoing to work...",
    "You won't need this. You're correct \nanyways. Always. This will be the last \nquestion. Goodbye. \n...\nI'm not crying... YOU'RE crying!"
    
]
happy_angry = [
    "Right, I guess...",
    "Splendid. Right answer.",
    "Oh, would you look at that?",
    "Did someone tell you the right \nanswer?",
    "Okay. Right answer.",
    "No comment... Fine. Correct."
]



dic = {
    "fråg1":{
        "Q": "First question, then...\nA semla is a traditional sweet roll that for instance is made in Sweden. If eaten together with warm milk, what is the Swedish word for it?",
        "svar": ["hetvägg","samke","grötbulle"],
        "template": [1,0,0],
    },
    "fråg2":{
        "Q": "Second question! In a 2010 study, people \nfound more mistakes when they marked essays \nwith a pen of what color?",
        "svar":["green","red","blue","magenta"],
        "template":[0,1,0,0],
    },
    "fråg3":{
        "Q": "Moving on to the third question! What \nprincess was traditionally called \nBadr al-Budur before Disney renamed her?",
        "svar":["jasmine","merida","anna","belle"],
        "template":[1,0,0,0],
    },
    "fråg4":{
        "Q": "Do you like the Swedish questions? In \nSwedish, a skvader is a rabbit with what \nunusual feature?",
        "svar":["wings","glasses","no ears","giant feet"],
        "template":[1,0,0,0],
    },
    "fråg5":{
        "Q": "More countries! Which country’s flag featuresan eagle eating a snake?",
        "svar":["mozambique","dominica","mexico","guam"],
        "template":[0,0,1,0],
    },
    "fråg6":{
        "Q": "Let's do a little TRUE or FALSE!\nThe kiwi fruit is native to New Zealand. True or false?",
        "svar":["True","False"],
        "template":[0,1],
    },
    "fråg7":{
        "Q": "What international retail chain got its start in Älmhult, Sweden, and runs a museum dedicated to its history there?",
        "svar":["H&M","Tesco","IKEA","Uniqlo"],
        "template":[0,0,1,0],
    },
    "fråg8":{
        "Q": "If you order “murgh” from the menu at an Indian restaurant, what meat will you get?",
        "svar":["Chicken","Beef","Duck","Venison"],
        "template":[1,0,0,0],
    },
    "fråg9":{
        "Q": "The first time someone bought real-world goods with bitcoins, 10,000 of them (worth over $90 million today) were exchanged for what?",
        "svar":["two pizzas","comic magazine","sneakers","luxury boat"],
        "template":[1,0,0,0],
    },
    "fråg10":{
        "Q": "Among land animals, what species has the largest eyes?",
        "svar":["tarsier","gibbon","owl","ostrich"],
        "template":[0,0,0,1],
    },
    "fråg11":{
        "Q": "So far, which continent has hosted the Olympics the most times?",
        "svar":["asia","europe","north america","africa"],
        "template":[0,1,0,0],
    },
    "fråg12":{
        "Q": "What app, a monster hit in 2016, has been credited with teaching Americans the metric system?",
        "svar":["Snapchat","Tinder","Pokemon GO","Google Maps"],
        "template":[0,0,1,0],
    },
    "fråg13":{
        "Q": "There are an estimated 1,864 of which bear species in the wild?",
        "svar":["Giant panda","White bear","Himalayan brown bear"],
        "template":[1,0,0],
    },
    "fråg14":{
        "Q": "What's the oldest continuously inhabited city in the world?",
        "svar":["Istanbul, Turkey","Jerusalem","Athens, Greece","Damascus, Syria"],
        "template":[0,0,0,1],
    },
}

frågor = -1
for fråga in dic:
    frågor += 1
angrsvar = -1
for svar in angry:
    angrsvar +=1
angrrsvar = -1
for svar in angry_angry:
    angrrsvar +=1
happrsvar = -1
for svar in happy_angry:
    happrsvar +=1


# n=1
# print(dic["fråg"+str(n)]["Q"])


    # "fråg":{
    #     "Q": "",
    #     "svar":["","","",""],
    #     "template":[],
    # },

    # "fråg":{
    #     "Q": "",
    #     "svar":["",""],
    #     "template":[],
    # },


#What international retail chain got its start in Älmhult, Sweden, and runs a museum dedicated to its history there?
#If you order “murgh” from the menu at an Indian restaurant, what meat will you get?
#The first time someone bought real-world goods with bitcoins, 10,000 of them (worth over US$90 million today) were exchanged for what?
#Among land animals, what species has the largest eyes?
#So far, which continent has hosted the Olympics the most times?
#What app, a monster hit in 2016, has been credited with teaching Americans the metric system?
#There are an estimated 1,864 of which bear species in the wild?
#What's the oldest continuously inhabited city in the world?