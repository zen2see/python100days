#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n")) 
numSymbols = int(input(f"How many symbols would you like?\n"))
numNumbers = int(input(f"How many numbers would you like?\n"))
genpwd = []
for x in range(numLetters):
    randLetter = letters[random.randint(0, len(letters)-1)]
    #randLetter = random.choice(letters)
    genpwd.append(randLetter)
    randSymbol = symbols[random.randint(0, len(symbols)-1)]
    genpwd.append(randSymbol)
    randNumber = numbers[random.randint(0, len(numbers)-1)]
    genpwd.append(randNumber)
random.shuffle(genpwd)
genpwd = ''.join(genpwd)
print(genpwd)
