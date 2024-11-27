from os import system, name
import random
import artblackjack

x = 1
players = []
dealer = []
playercards = []
dealercards = []
playerscore = -1 
dealerscore = -1
gameover = False
cardsl = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}


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
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
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
    return sum(cards)

def comparescores(playerscore, dealerscore):
    if playerscore == dealerscore:
        return "Draw "
    elif dealerscore == 0:
        return "Lose, opponent has Blackjack"
    elif playerscore == 0:
        return "Win you have Blackjack"
    elif playerscore > 21:
        return "Lose, you went over 21"
    elif dealerscore > 21:
        return "Opponent went over. You win"
    elif playerscore > dealerscore:
        return "You win!"
    else: 
        return "You lose!"

"""
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
    global gameover
    while not gameover:
        print(artblackjack.logo)
        blackjack()
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
            gameover = True
        else:
            dealagain = input("Type 'y' to get another card, type 'n' to pass: ")
            if dealagain == 'y':
                playercards.append(randomcard())
            else:
                gameover = True

playblackjack()
"""
def blackjack():
    global gameover
    print(artblackjack.logo)
    # playercards = []
    # dealercards = []
    # playerscore = -1 
    # dealerscore = -1
    # gameover = False
    for _ in range(2):
        playercards.append(randomcard())
        dealercards.append(randomcard())
    while not gameover:
        playerscore = calculate_score(playercards)
        print(f"Player's cards {playercards}, score {playerscore}")
        dealerscore = calculate_score(dealercards)
        # print(f"Dealer's cards {dealercards} score = {dealerscore}")
        print(f"Dealer 1st card {dealercards[0]}")
        if playerscore == 0 or dealerscore == 0 or playerscore > 21:
            gameover = True
        else:
            dealagain = input("Type 'y' to get another card, type 'n' to pass: ")
            if dealagain == 'y':
                playercards.append(randomcard())
            else:
                gameover = True
    while dealerscore != 0 and dealerscore < 17:
        dealercards.append(randomcard)
        dealerscore = calculate_score(dealercards)
        print(f"Dealer's cards {dealercards}, score: {dealerscore}")

    print(f"Your final hand: {playercards}, final score: {playerscore}")
    print(f"Dealers final hand: {dealercards}, final score: {dealerscore}")
    print(comparescores(playerscore, dealerscore))
    #       for _ in range(2):
            # for n in players:
            # players.append(playercards.append[randomcard()])
            # print(f"Player{n}'s card {players[n]}")
    #        playercards.append(randomcard())
    #         dealercards.append(randomcard())
        

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear()
    blackjack()
    



        
