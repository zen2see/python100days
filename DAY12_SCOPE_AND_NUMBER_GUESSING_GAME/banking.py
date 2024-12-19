import datetime
import random
import artbanking
import sys
import curses
import time

# Banking Guessing Game!
attempts = 0
guess = 0
number = random.randint(1, 100)
EASY_LEVEL = 10
HARD_LEVEL = 5
firstrun = True
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

def clear_part(lines):
    for _ in range(lines):
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

# def clear_part(stdscr):
#     for i in range(y, y + height):
#         stdscr.addstr(i, x, " " * width)
#     stdscr.refresh()

def playagain():
    again = input("Play again - 'y' or 'n': ").lower()
    if again == 'y':
        main()
    else:
        exit()
        
def set_difficulty():
    global firstrun
    firstrun = False
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else: 
        return HARD_LEVEL

def check_answer(guess, number, attempts):
    clear_part(4)
    while attempts > -1:
        if guess > number:
            attempts -= 1
            print("Too high.\nGuess again.\n")
            guess_number(attempts)
        elif guess < number:
            attempts -= 1
            print("Too low.\nGuess again.\n")
            guess_number(attempts)
        else:
            won()
        print("You ran out of guesses!")
        lost() 


def lost():
    print("You lost!")
    exit()

def won():
    print("YOU GUESSED THE NUMBER!")
    playagain() 

def guess_number(attempts):
    if firstrun == False:
        clear_part(2)
    print(f"\nYou have {attempts} remaining chances to guess the number")
    guess = int(input(f"Make a guess: "))
    check_answer(guess, number, attempts)

def main(): 
    # clock()
    print(artbanking.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    global attempts
    attempts = set_difficulty()
    guess_number(attempts)

if __name__ == "__main__":
    main()