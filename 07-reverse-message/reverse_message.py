#Seth Camomile
#Period 7

def reverse(message):
    rep = message[::-1]
    return rep

def main():
    message = input("What is your message?\n")
    print(reverse(message))
