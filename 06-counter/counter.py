#Seth Camomile
#Period 7

def count(start, end, step):
    rep = ''
    for i in range(start, end + (-1 if step < 0 else 1), step):
        rep += str(i) + ' ' #you still have to add a space at the end just because of the tests
    return rep


def main():
    start = int(input("What is the starting number? "))
    end = int(input("What is the ending number? "))
    step = int(input("How much should I cound by? "))
    print(count(start,end,step))
