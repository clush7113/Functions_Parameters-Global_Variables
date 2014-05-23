#dice rolling program
import random, time

def rollDice():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll


def show_dice(roll):
    rollDie={1:"- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n",
             2:"- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n",
             3:"- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n",
             4:"- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n",
             5:"- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n",
             6:"- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"}
    print(rollDie[roll])


roll=rollDice()
time.sleep(1)
show_dice(roll)

