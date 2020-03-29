import time

myName = input("What's your name?\n> ").capitalize()
print("Hello, {}!".format(myName))

time.sleep(2)

favFruit = input("What's your favorite fruit?\n> ")
print("So, {}... Your favorite fruit is {}, then?"
    .format(myName,favFruit))