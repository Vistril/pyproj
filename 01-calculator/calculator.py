#Seth Camomile
#Period 7

def math(a,b):
    a = int(a)
    b = int(b)
    add = a + b #do addition
    sub = a - b #do subtraction
    mul = a * b #do multiplication
    div = round(a/b, 2) #do division, round to 2 decimal places
    flr = a // b #do floor division
    mod = a % b #do modulus division
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    return rep

def main():
    a = int(input("Input an integer: ")) #get a number from the user
    b = int(input("Input another integer: ")) #get another number from the user
    print(str(math(a,b)))
