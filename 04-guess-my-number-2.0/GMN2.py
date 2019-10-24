#Seth Camomile
#Period 7 

import random

def get_guess():
    user = int(input("Take a guess: "))
    return user

def hi_low(user, the_number, tries):
    if tries != 5:
        if user > the_number:
            return "High", True
        elif user < the_number:
            return "Low", True
        else:
            return "Correct", False
    elif tries == 5:
        if user > the_number:
            return "High", False
        elif user < the_number:
            return "Low", False
        else:
            return "Correct", False

def end(tries, hl, the_number):
    if tries > 5 or hl == "Low" or hl == "High":
        return f"You ran out of tries! The number was {the_number}"
    else:
        return f"You guessed it in {tries} tries! The number was {the_number}"

def main():
    print("I'm thinking of a number between 1 and 100")
    print("You have 5 attemps to guess my number.")
    the_number = random.randint(1,100)
    play = True
    tries = 0
    while play and tries < 5:
        tries += 1
        print(f"Guess number {tries}")
        user = get_guess()
        hl, play = hi_low(user, the_number, tries)
        print(f"Your guess was {hl}")
    print(end(tries, hl, the_number))