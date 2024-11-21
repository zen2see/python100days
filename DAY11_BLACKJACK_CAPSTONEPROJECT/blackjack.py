from os import system, name
import random
import artblackjack

x = 1
players = []
dealer = []
playercards = []
dealercards = []
cardsl = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}
gameover = False

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def randomcard():
    """
    Returns a random card from the deck
    # Get random dictionary pair in dictionary
    # Using random.choice() + list() + items()
    # random_card = random.choice(list(cards.items()))
    # OR random.choice(cards)
    """ 
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
    card = random.choice(cards)
    # print("The random card is " + str(random_card))
    # print(random_card[0])
    # print(random_card[1])
    return card

def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum (cards)

def comparescores(playerscore, dealerscore):
    if playerscore == dealerscore:
        return "Draw "
    elif dealerscore == 0:
        return "Lose, opponent has Blackjack"
    elif playerscore == 0:
        return "Win you have Blackjack"

def playblackjack():
    play = input("New player? Join a game of Blackjack? Type 'y' or 'n' ").lower()
    if play == 'y':
        players.append(1)
        clear()
        playblackjack()
    elif play == 'n' and players == 0:
       quit()
    else:
        blackjack()

def blackjack():
    print(artblackjack.logo)
    # print(randomcard())
    # dealer.update(randomcard())
    for _ in range(2):
         # for n in players:
         # players.append(playercards.append[randomcard()])
         # print(f"Player{n}'s card {players[n]}")
         playercards.append(randomcard())
         dealercards.append(randomcard())
        
    playerscore = calculate_score(playercards)
    print(f"Player's cards {playercards} score = {playerscore}")
    dealerscore = calculate_score(dealercards)
    print(f"Dealer's cards {dealercards} score = {dealerscore}")
    if playerscore == 0 or dealerscore == 0 or playerscore > 21:
        game_over = True
    else:
        dealagain = input("Type 'y' to get another card, type 'n' to pass: ")
        if dealagain == 'y':
            playercards.append(randomcard())
        else:
            gameover = True

while not gameover:
    playblackjack()

    
