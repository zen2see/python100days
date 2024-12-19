import random
import artbanking

# Banking Guessing Game!
attempts = 0
guess = 0
number = random.randint(1, 100)
EASY_LEVEL = 10
HARD_LEVEL = 5

def playagain():
    again = input("Play again - 'y' or 'n': ").lower()
    if again == 'y':
        main()
    else:
        exit()
        
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
        return EASY_LEVEL
    else: 
        return HARD_LEVEL

def check_answer(guess, number, attempts):
    attempts
    while attempts > -1:
        if guess > number:
            attempts -= 1
            print("Too high.\nGuess again.\n")
            guess_number(attempts)
        elif guess < number:
            attempts -= 1
            print("Too low.\nGuess again.\n")
            guess_number()
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

def guess_number():
    print(f"\nYou have {attempts} remaining chances to guess the number")
    guess = int(input(f"Make a guess: "))
    check_answer(guess, number, attempts)
    # check_answer(guess, number, attempts)
    # while attempts > 0:
    #     if guess > number:
    #         attempts -= 1
    #         print("Too high.\nGuess again.\n")
    #         guess_number()
    #     elif guess < number:
    #         attempts -= 1
    #         print("Too low.\nGuess again.\n")
    #         guess_number()
    #     else:
    #         won()
    #     print("You ran out of guesses!")
    #     lost() 

def main(): 
    print(artbanking.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    global attempts
    attempts = set_difficulty()
    guess_number()

if __name__ == "__main__":
    main()