#Seth Camomile
#Period 7  
import random

def coin(flips):
    if flips < 0:
        return 0, 0, 0
    count = 0
    heads = 0
    tails = 0
    for i in range(flips):
        r = random.randint(0, 1)
        if r == 1:
            heads += 1
        elif r == 0:
            tails += 1
    count = flips
    return count, heads, tails

def main():
    flips = int(input("How many coin flips do you want?"))
    c,h,t = coin(flips)
    print(f"The coin has been flipped {c} times.\nHeads: {h}\t Tails: {t}")
