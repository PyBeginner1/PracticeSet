import random

roll_again = 'yes'

while roll_again == 'yes':
    print("Rolling the dice...")

    dice1= random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The values are:")
    print("Dice 1:", dice1 , "\nDice 2:", dice2)

    if dice1 == dice2:
        print("You rolled double")
    else:
        print("Next time")
    roll_again = input("Do you wanna play?")

