#dice rolling program
import random, time

def rollDice():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll


def showDice(roll):
    rollDie={1:"- - - - -\n|     |\n|  O  |\n|     |\n- - - - -\n",
             2:"- - - - -\n|  O  |\n|     |\n|  O  |\n- - - - -\n",
             3:"- - - - -\n| O   |\n|  O  |\n|  O  |\n- - - - -\n",
             4:"- - - - -\n| O O |\n|     |\n| O O |\n- - - - -\n",
             5:"- - - - -\n| O O |\n|   O |\n| O O |\n- - - - -\n",
             6:"- - - - -\n| O O |\n| O O |\n| O O |\n- - - - -\n"}
    print(rollDie[roll])

roll=rollDice()
time.sleep(1)
showDice(roll)

###################################################################

roll=rollDice()
time.sleep(1)
showDice(roll)

def rollTwice():
    prevRoll=7
    roll=0
    while True:
        roll=rollDice()
        time.sleep(1)
        showDice(roll)
        if roll==prevRoll:
            break
        prevRoll=roll

def rollSix():
    roll=int()
    while True:
        roll=rollDice()
        time.sleep(1)
        showDice(roll)
        if roll==6:
            print("Found")
            break

def rollSixTwice():
    prevRoll=7
    roll=0
    while True:
        roll=rollDice()
        time.sleep(1)
        showDice(roll)
        if roll==prevRoll and roll==6:
            break
        prevRoll=roll

def main():
    rollSix()
    rollTwice()
    rollSixTwice()

main()

##Corrected syntax e.g. replaced else with elif, fixed spelling, corrected operators
##Moved dice strings to show dice function
##Put dice strings into dictionary
##Removed if statment, replaced with dictionary look-up
##Added new functions
