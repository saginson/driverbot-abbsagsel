
angry = [
    "Oh no. You didn't actually know the answer?",
    "Another answer you didn't know, huh?",
    "OF COURSE you didn't know the answer! Why do I even bother with you?",
    "WHY CAN'T YOU JUST BE SMART LIKE YOUR \nSIBLINGS?! *cough* *cough* It's fine. I'm \nFINE.",
    "*Heavy breathing*",
    "I don't know... Is this even worthwhile? I mean, you clearly aren't learning anything.",
    "I knew you'd get this one wrong."
    
]
angry_angry = [
    "WHY CAN'T YOU JUST BE SMART LIKE YOUR \nSIBLINGS?! *cough* *cough* You know what? \nFine. The right answer to the next question \nis number three. Mexico. Número tres."
]
happy = [
    "Correct answer!",
    "Wow! Another correct answer!",
    "I didn't expect that you'd be so good at this!",
    "Correct! How admirable! *swoons*",
    "Oh mah God! CAN I ADOPT YOU?!",
    "You must be a MASTERMIND! *applause*",
    "Honestly, I think the only right decision would be to change positions..."
    
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
        "svar":["two pizzas","a novelty calendar","sneakers","luxury boat"],
        "template":[1,0,0,0],
    },
}
# n=1
# print(dic["fråg"+str(n)]["Q"])

# :{
#         "Q": "",
#         "svar":[],
#         "template":[],
#     },



#What international retail chain got its start in Älmhult, Sweden, and runs a museum dedicated to its history there?
#If you order “murgh” from the menu at an Indian restaurant, what meat will you get?
#The first time someone bought real-world goods with bitcoins, 10,000 of them (worth over US$90 million today) were exchanged for what?