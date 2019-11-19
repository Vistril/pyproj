#Name
#Period

vowel = ['a','e','i','o','u']
punct = ['!','.',',']

def translator(message):
    word = message.split(' ')
    pig = ''
    for k in word:
        if k[0] in vowel:
            pig += way_end(k)
        elif k[0] not in vowel:
            for i in k:
                if i in vowel:
                    position = k.index(i)
                    pig += ay_end(k, position)
                    break
    return pig.lower()

def way_end(message):
    if message[-1] in punct:
        return message[0:-1] + "way" + message[-1] + " "
    return message + "way "

def ay_end(message, position):
    if message [-1] in punct:
        return message[position:-1] + message[:position] + "ay" + message[-1] + " "
    return message[position:] + message[:position] + "ay "

def main():
  print("Welcome to the Pig Latin Translator!")
  message = input("Please enter a word to translate:\n")
  pig = translator(message)
  print(f"The translation is:\n\n{pig}")
  print("\nGoodbye!")

if __name__ == '__main__':
    main()
