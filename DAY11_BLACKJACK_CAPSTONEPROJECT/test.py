from os import system, name
import random
import artblackjack


playercards = []
dealercards = []
playerscore = -1 
dealerscore = -1
gameover = False

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

def comparescores(pscore, dscore):
    if pscore == dscore:
        return "Draw "
    elif dscore == 0:
        return "Lose, opponent has Blackjack"
    elif pscore == 0:
        return "Win you have Blackjack"
    elif pscore > 21:
        return "Lose, you went over 21"
    elif dscore > 21:
        return "Opponent went over. You win"
    elif pscore > dscore:
        return "You win!"
    else: 
        return "You lose!"


print(f"Your final hand: {playercards}, final score: {playerscore}")
print(f"Dealers final hand: {dealercards}, final score: {dealerscore}")
print(comparescores(playerscore, dealerscore))




"""
def calculate_score(cards):
 
    Take a list of cards and return the score calculated from the cards
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)     
"""






# calculate_score
