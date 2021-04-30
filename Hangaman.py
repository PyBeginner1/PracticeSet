import random

words=['tired','jeans','educate','arrive','outrageous','stocking','blink','ambitious','shoes','dirty']
word=random.choice(words)
allowed_errors= 7
guesses = []
done =False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(" ")



    guess = input(f"You have {allowed_errors} attempts left. Next guess:")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break


    done= True
    for letter in word:
        if letter.lower() not in guesses:
            done=False

if done:
    print(f"You guessed it. It was {word}")
else:
    print(f"Wrong. It was {word}")