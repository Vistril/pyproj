#Seth Camomile
#Period 7
 
import random
import math
#feel free to change the words to what your want
WORDS = ("python",
        "jumble",
        "easy",
        "difficult",
        "answer",
        "xylophone")
HINTS = ("Something","An idea")
 
 
def setup(WORDS, HINTS):
    # pick one word randomly from the sequence
    word = random.choice(WORDS)
    # make word and hint parallel
    hint = HINTS[WORDS.index(word)]
    # create a variable to use later to see if the guess is correct
    correct = word
    # create a jumbled version of the word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return correct, jumble, hint
 
def guessing(correct, guess, hint, hint_used):
    if guess == correct:
        rep = "That's it!  You guessed it!\n"
        playing = False
    elif guess == "hint":
        rep = hint
        playing = True
        hint_used = True
    else:
        rep = "That's not it. Try again.\nType 'hint' if you want a hint."
        playing = True
    return playing, rep, hint_used
 
def end(hint_used):
    if hint_used == False:
        return "Good job not using a hint!\nThanks for playing."
    elif hint_used == True:
        return "Try to not use a hint next time.\nThanks for playing."
 
def main():
    correct, jumble, hint = setup(WORDS, HINTS)
    playing = True
    hint_used = False
    # start the game
    print(
    """
           Welcome to Word Jumble!
 
   Unscramble the letters to make a word.""")
    print("The jumble is:", jumble)
    while playing:
        guess = input("Your guess: ")
        playing, text, hint_used = guessing(correct, guess, hint, hint_used)
        print(text)
    print(end(hint_used))