from gamedata import data 
from higherlowerlogo import higherlowerlogo as hllogo
from vslogo import vslogo 
import random

""" From the list of unicodes, replace “+” with “000”. https://home.unicode.org/ www.unicode.org/
 example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it. """

ans = "" 
score = 0
should_continue = True
random_topic1 = random.choice(data)
random_topic2 = random.choice(data)

# Display Logo
def printlogo():
    print(hllogo)
    
# Get Random Topics
def randomtopics():
    random_topic1 = random.choice(data)
    random_topic2 = random.choice(data)
    return random_topic1, random_topic2

# Compare Topics 
def compareT():
   print(f"A: {random_topic1['name']}, a {random_topic1['description']}, from {random_topic1['country']}.")
   print(vslogo)
   print(f"B: {random_topic2['name']}, a {random_topic2['description']}, from {random_topic2['country']}.") 

# Ask Question
def askq():
    global ans 
    ans = input("\nWho has more followers? Type 'A' or 'B': ").lower()

# Display Results
def results():
    return max(random_topic1['follower_count'],random_topic2['follower_count'])

def check():
    global should_continue, score
    if (results() == random_topic1['follower_count']) & (ans == 'a'):
        print("Correct! \U0001F600")
        score += 1
    elif (results() == random_topic2['follower_count']) & (ans == 'b'):
        print("Correct! \U0001F600")
        score += 1
    else:
        print("Incorrect \U0001F641")
    print(f"{random_topic1['follower_count']} vs. {random_topic2['follower_count']}")
    print("Score is ", score)
    cont = input("Should we continue? 'Y' or 'N': ").lower()
    if cont == 'y':
        should_continue = True
    else: 
        should_continue = False

def main():
    printlogo()
    while should_continue == True:
        global random_topic1, random_topic2
        random_topic1 = random_topic2 
        random_topic2 = random.choice(data)
        if random_topic1 == random_topic2:
          random_topic2 = random.choice(data)
        compareT()
        askq()
        check()

if __name__ == '__main__':
    main()
    