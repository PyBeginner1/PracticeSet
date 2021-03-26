import random

print("Rock, Paper, Scissors!!!")
def play():
    user = input("Enter Rock, paper, Scissors:").lower()
    computer = random.choice(["rock","paper","scissor"])

    if computer == "rock":
        if user == "paper":
            print(f"Congrats you won, my guess was {computer} and you guessed {user}")
        elif user == "scissor":
            print(f"You lost my guess was {computer}")
        else:
            print("Its a tie")

    elif computer == "paper":
        if user == "scissor":
            print(f"Congrats you won, my guess was {computer} and you guessed {user}")
        elif user == "rock":
            print(f"You lost my guess was {computer}")
        else:
            print("Its a tie")

    elif computer == "scissor":
        if user == "rock":
            print(f"Congrats you won, my guess was {computer} and you guessed {user}")
        elif user == "paper":
            print(f"You lost my guess was {computer}")
        else:
            print("Its a tie")

play()


