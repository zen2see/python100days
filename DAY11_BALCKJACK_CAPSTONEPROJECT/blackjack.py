from os import system, name
import artblackjack

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

player1 = []
player2 = []
dealer = {}
def playblackjack():
    cards = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11} 
    random_card = random.choice(cards[key])

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if play == 'y':
    clear()
    playblackjack()


    
