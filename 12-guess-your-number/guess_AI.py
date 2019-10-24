#Name
#Period
import random

def end(tries, user):
    return ""

def high_low(low, high, guess, user, tries, play):
    return 1, 2, 1, False


def main():
    print("I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.")
    print("After each guess, tell me if I'm 'high', 'low', or 'correct'.")

    high = 100
    low = 1
    play = True
    guess = random.randint(low,high)
    tries = 1
    user = ''
    while play:
        print(f"For try {tries} I guess {guess}")
        user = ''
        while user not in ('high','low','correct'):
            user = input("Am I 'high', 'low', or 'correct'? ")
        low, high, tries, play = high_low(low, high, guess, user, tries, play)
        guess = random.randint(low, high)
    print(end(tries, user))
