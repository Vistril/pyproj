#Mr. Simonsen
#14



def main():
  print("Welcome to the Pig Latin Translator!")
  message = input("Please enter a word to translate:\n")
  pig = translator(message)
  print(f"The translation is:\n\n{pig}")
  print("\nGoodbye!")

if __name__ == '__main__':
    main()
