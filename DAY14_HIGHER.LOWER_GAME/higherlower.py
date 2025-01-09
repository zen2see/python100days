from os import system, name
from gamedata import data 
from higherlowerlogo import higherlowerlogo as hllogo
from vslogo import vslogo 
import random

""" From the list of unicodes, replace “+” with “000”. https://home.unicode.org/ www.unicode.org/
 example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it. """

# Clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Display Logo
def printlogo():
    print(hllogo)
    
# Get Random Topics
def randomtopics():
    random_topic1 = random.choice(data)
    random_topic2 = random.choice(data)
    return random_topic1, random_topic2

# Compare Topics 
def compareT(random_topic1, random_topic2):
   print(f"A: {random_topic1['name']}, a {random_topic1['description']}, from {random_topic1['country']}.")
   print(vslogo)
   print(f"B: {random_topic2['name']}, a {random_topic2['description']}, from {random_topic2['country']}.") 

# Ask Question
def askq():
    ans = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    return ans

# Display Results
def results(random_topic1, random_topic2):
    return max(random_topic1['follower_count'],random_topic2['follower_count'])

def check(random_topic1, random_topic2, ans, score):
    if (results(random_topic1, random_topic2) == random_topic1['follower_count']) & (ans == 'a'):
        print("Correct! \U0001F600")
        score += 1
    elif (results(random_topic1, random_topic2) == random_topic2['follower_count']) & (ans == 'b'):
        print("Correct! \U0001F600")
        score += 1
    else:
        print("Incorrect \U0001F641")
    print(f"{random_topic1['follower_count']} vs. {random_topic2['follower_count']}")
    print("Score is ", score)
    cont = input("Should we continue? 'Y' or 'N': ").lower()
    should_continue = cont == 'y'
    if cont == 'y':
        should_continue = True
    else: 
        should_continue = False
    return should_continue, score

def main():
    printlogo()
    score = 0
    should_continue = True
    random_topic1, random_topic2 = randomtopics()
    while should_continue == True:
        random_topic1 = random_topic2 
        random_topic2 = random.choice(data)
        if random_topic1 == random_topic2:
          random_topic2 = random.choice(data)
        compareT(random_topic1, random_topic2)
        ans = askq()
        should_continue, score = check(random_topic1, random_topic2, ans, score)
        clear()

if __name__ == '__main__':
    main()
    