#Seth Camomile
#Period 7 

import random as r
 
def roll(num, d):
    sum = 0
    for i in range(num):
        value = r.randint(1, d)
        print(f"Roll {i+1}: {value}")
        sum += value

    return sum

def main():
    num = int(input("How many dice would you like to roll? "))
    d = int(input ("How many sides does the dice have? "))
    print(f"Rolling {num}x d{d}")
    print(f"Total: {roll(num,d)}")
