from glob import escape, glob
import time
import random
from tracemalloc import stop 


print("Hello, welcome to the hellavator")
print("^^^^^^^^^^^^^^^" * 5)

global play
level = 0
play = 1
UPAMOUNT = 0
DOWNAMOUNT = 0
numbers = 0
score = 0

def DEVILGAME():

    print("You dare enter my lair?")
    print("FOR THIS YOU SHALL PAY \n" * 3)
    lives = 3
    escape = False
    while lives > 0 and escape == False:
            numbers = random.randint(1, 5)
            print("pick a number between 1 and 5, this shall decide your fate")
            guess = int(input(""))
            if numbers == guess:
                global score
                print("You are a magician holy shit, get out of my bedroom")
                score+=5
                print("For passing my level i might aswell award you 5 points, here you go")
                print("Your score is now ", score)
                escape = True
            else:
                print("You are a spastic")
                time.sleep(0.5)
                lives-=1
                print("You have ", lives, " lives left, be wise with your next decision")
                if lives <= 0:
                    exit
    if lives <= 0:
        print("YOU FAILED AND PERISHED IN MY ASSHOLE AFTER I ATE TACOBELL")
        exit()
    
    else:
        exit
        

def GODGAME():
    global score
    print("Hello my friend, even though i am not real i shall increase your score")
    score+=1
    print("Your score is now", score)
    time.sleep(0.5)
    print("now do you dare venture further down? Maybe knowing more points await you there will encouarge you")



print("You are on level ", level)

while play == 1 and score < 20:
    print("Where would you like to go?")
    print("UP/DOWN    or    stop")
    UPDOWN = str(input(""))

    if UPDOWN == "UP".lower():
        UPAMOUNT = int(input("By how much? \n"))
        level+=UPAMOUNT
        print("\n \n \n", "   You are on level ", level)
        if level >= 100:
            print("You have reached GOD, he welcomes you with his loveley embrace")
            GODGAME()

    elif UPDOWN == "DOWN".lower():
        DOWNAMOUNT = int(input("By how much? \n"))
        level-=DOWNAMOUNT
        print("\n \n \n", "   You are on level ", level)
        if level <= -100:
            print("You have reached the DEVIL, he welcomes you with fiery palms")
            DEVILGAME()
    elif UPDOWN == "stop":
        play = 0

    else:
        print("\n \n \n \n \n Learn to spell")
        time.sleep(1)
print("You have either won or left, either way i cant be asked to create a function to find out, well done anyway")