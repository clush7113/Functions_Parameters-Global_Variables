#dice rolling program
import random, time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def rollDice():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll


def show_dice(roll):
    rollDie={1:s1,2:s2,3:s3,4:s4,5:s5,6:s6}
    print(rollDie[roll])


roll=rollDice()
time.sleep(1)
show_dice(roll)

