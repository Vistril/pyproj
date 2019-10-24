#Seth Camomile
#Period 7

import random
import math

def scrambler(words):
    random.shuffle(words)
    return ' '.join(words) + ' ' #need another trailing space because of tests, i'm not that accurate

def splitter(message):
    words = message.split(' ')
    num_words = len(words)
    #del words[-1] 
    return words, num_words

def main():
    message = input("What is the message to scrable?\n")
    words, num_words = splitter(message)
    print(f"There are {num_words} words in the message")
    print("Here they are shuffled:")
    print(scrambler(words))
