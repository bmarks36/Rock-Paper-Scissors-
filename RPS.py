from time import sleep
from random import randint
def RPS():
    seconds = 1.0
    decisions = ["Rock", "Paper", "Scissors"]
    yourScore = 0
    compScore = 0
    #player = False
    #while player == False: # no value is assigned to it so its false
    while yourScore < 2 or compScore < 2:
        player = input("Rock, Paper, Scissors? ")
        comp = decisions[randint(0,2)]#used to give a random number from 0 to 2 to choose from
        if player == comp:
            print("compChoice = {}".format(comp))
            sleep(seconds)
            print("Issa tie shawty. Less go again")
            sleep(seconds)
            print("compScore = {}".format(compScore))
            print("yourScore = {}".format(yourScore))
            sleep(seconds)
        elif player == "Rock": #their choice given  
            if comp == "Paper":
                compScore = compScore + 1
                print("compChoice = {}".format(comp))
                sleep(seconds)
                print("Shawty dis paper cover rock all day. I win")
                sleep(seconds)
                print("compScore = {}".format(compScore))
                print("yourScore = {}".format(yourScore))
                if yourScore == 2:
                    sleep(seconds)
                    print("whatever. you won 2/3")
                    break
                elif compScore == 2:
                    sleep(seconds)
                    print("that's what i thought. I WIN SHAWTY. 2/3!")
                    break
                else:
                    sleep(seconds)
            elif comp == "Scissors":
                yourScore += 1
                print("compChoice = {}".format(comp))
                sleep(seconds)
                print("Fine shawty, stomp on me den. You win")
                sleep(seconds)
                print("compScore = {}".format(compScore))
                print("yourScore = {}".format(yourScore))
                if yourScore == 2:
                    sleep(seconds)
                    print("whatever. you won 2/3.")
                    break
                elif compScore == 2:
                    sleep(seconds)
                    print("that's what i thought. I WIN SHAWTY. 2/3!")
                    break
                else:
                    sleep(seconds)
        elif player == "Paper":
            if comp == "Rock":
                yourScore += 1
                print("compChoice = {}".format(comp))
                sleep(seconds)
                print("you win that one ig.")
                sleep(seconds)
                print("compScore = {}".format(compScore))
                print("yourScore = {}".format(yourScore))
                if yourScore == 2:
                    sleep(seconds)
                    print("whatever. you won 2/3")
                    break
                elif compScore == 2:
                    sleep(seconds)
                    print("that's what i thought. I WIN SHAWTY. 2/3!")
                    break
                else:
                    sleep(seconds)
            elif comp == "Scissors":
                compScore += 1
                print("compChoice = {}".format(comp))
                sleep(seconds)
                print("I win. HA")
                sleep(seconds)
                print("compScore = {}".format(compScore))
                print("yourScore = {}".format(yourScore))
                if yourScore == 2:
                    print("whatever. you won 2/3.")
                    break
                elif compScore == 2:
                    print("that's what i thought. I WIN SHAWTY. 2/3!")
                    break
                else:
                    sleep(seconds)
        elif player == "Scissors":
            if comp == "Rock":
                compScore += 1
                print("compChoice = {}".format(comp))
                sleep(seconds)
                print("broke dat NECK. I WIN")
                sleep(seconds)
                print("compScore = {}".format(compScore))
                print("yourScore = {}".format(yourScore))
                if yourScore == 2:
                    sleep(seconds)
                    print("whatever. you won 2/3.")
                    break
                elif compScore == 2:
                    sleep(seconds)
                    print("that's what i thought. I WIN SHAWTY. 2/3!")
                    break
                else:
                    sleep(seconds)
            elif comp == "Paper":
                yourScore += 1
                print("compChoice = {}".format(comp))
                sleep(seconds)
                print("whatever.you won that one.")
                sleep(seconds)
                print("compScore = {}".format(compScore))
                print("yourScore = {}".format(yourScore))
                if yourScore == 2:
                    sleep(seconds)
                    print("whatever. you won 2/3.")
                    break
                elif compScore == 2:
                    sleep(seconds)
                    print("that's what i thought. I WIN SHAWTY. 2/3!")
                    break
                else:
                    sleep(seconds)
    answer = input("Do you want to play again? (Yes or No) ")
    if answer.lower() == "yes":
        print("Okayyy!")
        sleep(seconds)
        RPS()
    elif answer.lower() == "no":
        print("You're just scared. But, I had fun :)")
        sleep(seconds)
        print("See you next time!")
    
                
                    
            
        
        
