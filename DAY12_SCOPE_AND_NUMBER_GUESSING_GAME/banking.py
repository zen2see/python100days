import random
import artbanking

# Banking Guessing Game!
attempts = 0
guess = 0
number = random.randint(1, 100)

def main():    
    print(artbanking.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    set_difficulty()
    guess_number()

def playagain():
    again = input("Play again - 'y' or 'n': ").lower()
    if again == 'y':
        main()
    else:
        exit()
        
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    global attempts
    if difficulty == "easy":
        attempts = 10
    else: 
        attempts = 4

def lost():
    print("You lost!")
    exit()

def won():
    print("YOU GUESSED THE NUMBER!")
    playagain() 

def guess_number():
    global attempts
    print(f"\nYou have {attempts} remaining chances to guess the number")
    guess = int(input(f"Make a guess: "))
    while attempts > -1:
        if guess > number:
            print("Too high.\nGuess again.\n")
            guess_number()
        elif guess < number:
            print("Too low.\nGuess again.\n")
            guess_number()
        else:
            won()
        print("You ran out of guesses!")
        lost() 

if __name__ == "__main__":
    main()