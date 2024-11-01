import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose?\n0 = Rock\n1 = Paper\n2 = Scissors\n\r"))
randChoice = random.randint(0,2)

hands = [rock, paper, scissors]
status = ""
if choice == 0:
    if randChoice == 0:
        status = "Tied"
    elif randChoice == 1:
        status = "Lost"
    else:
        status = "Won"
elif choice == 1:
    if randChoice == 0:
        status = "Won"
    elif randChoice == 1:
        status = "Tied"
    else:
        status ="Lost"
else:
    if randChoice == 0:
        status = "Lost"
    elif randChoice == 1:
        status = "Won"
    else:

        status = "Tied"
print("You chose: \n", hands[choice])
print("Computer chose: \n", hands[randChoice])
print("You ", status)
