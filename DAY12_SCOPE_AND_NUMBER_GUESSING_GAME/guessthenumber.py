import datetime
import random
import artbanking
import sys
import time

# Banking Guessing Game!
attempts = 0
guess = 0

EASY_LEVEL = 10
HARD_LEVEL = 5
firstrun = True
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

def getRandomNum():
    num = random.randint(1, 100)
    return num

def clear_part(lines):
    for _ in range(lines):
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

def playagain():
    again = input("Play again - 'y' or 'n': ").lower()
    if again == 'y':
        main()
    else:
        exit()
        
def set_difficulty(firstrun):
    firstrun = False
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else: 
        return HARD_LEVEL

def check_answer(guess, number, attempts):
    clear_part(4)
    while attempts > 0:
        if guess > number:
            attempts -= 1
            print(guess, "Too high. Guess again:\n")
            guess_number(attempts, number)
        elif guess < number:
            attempts -= 1
            print(guess, "Too low. Guess again:\n")
            guess_number(attempts, number)
        else:
            won()
        print("You ran out of guesses!")
        lost(number) 

def lost(num):
    print("You lost!")
    print("It was ", num)
    exit()

def won():
    print("YOU GUESSED THE NUMBER!")
    playagain() 

def guess_number(attempts, number):
    # if firstrun == False:
    #     clear_part(2)
    print(f"You have {attempts} remaining chances to guess the number")
    guess = int(input(f"Make a guess: "))
    check_answer(guess, number, attempts)

def main(): 
    # clock()
    number = getRandomNum()
    print(artbanking.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    # global attempts
    attempts = set_difficulty(firstrun)
    guess_number(attempts, number)

if __name__ == "__main__":
    main()