#Seth Camomile
#Period 7

import random as r

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        self.name = name
        self.hunger = r.randint(0, 10)
        self.boredom = r.randint(0, 10)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
      rep = "Critter Object\n"
      rep += f"Name: {self.name}\nHunger: {self.hunger}\nBoredom: {self.boredom}\nMood: {self.mood}\n"
      return rep

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        rep = f"I'm {self.name} and I feel {self.mood} now.\n"
        self.__pass_time()
        return rep

    def eat(self, foodCount):
        self.hunger -= foodCount
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        return "Brruppp.  Thank you."

    def play(self, playCount):
        self.boredom -= playCount
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        return "Wheee!"


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print 
        ("""
        Critter Caretaker
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            print(crit.talk())

        # feed your critter
        elif choice == "2":
            amt = input("How much would you like to feed your critter?")
            print(crit.eat(amt))

        # play with your critter
        elif choice == "3":
            amt = input("How much would you like to play?")
            print(crit.play(amt))

        # secret backdoor
        elif choice == '14':
            print(crit)
        # some unknown choice
        else:
            print(f"\nSorry, but {choice} isn't a valid choice.")
