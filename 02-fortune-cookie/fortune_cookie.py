#Name
#Period
import random

f1 = "Help! I’m being held prisoner in a fortune cookie bakery!"
f2 = "Cookie said: \"You really crack me up.\""
f3 = "You are not illiterate."
f4 = "You will read this and say \"Geez! I could come wp with better fortunes than that!\""
f5 = "This cookie is never gonna give you up, never gonna let your down."

def cookie():
    resp = [f1, f2, f3, f4, f5]
    return random.choice(resp) #probably not how we're supposed to do it but it works so..

def main():
    print("You crack open the cooke and your fortune falls out:")
    print(cookie())
