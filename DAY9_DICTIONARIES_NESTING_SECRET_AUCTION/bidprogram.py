import os

# Create an empty dictionairy
bids = {}
continue_bids = True

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS and Linux
    else:
        os.system('clear')

# Compare bids
def highest_bidder(bidderdictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidderdictionary:
        bid_amount = bidderdictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        # OR max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of bid of ${highest_bid}")

while continue_bids:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # Add bids
    bids[name] = price
    # Any other bids
    more_bids = input("Are there any other bidders? 'yes' or 'no' \n").lower()
    if more_bids == "no":
        continue_bids = False
        highest_bidder(bids)
    elif more_bids == "yes":
        # Clear screen
        # print("\n" * 20)
        clear_screen()


