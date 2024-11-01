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
choice = input("What do you choose?\n0 = Rock\n1 = Paper\n2 = Scissors\n\r")
randChoice = random.randint(1,3)
status = ""
phand = ""
chand = ""
if choice == "0":
    phand = rock
    if randChoice == 0:
        chand = rock
        status = "Tied"
    elif randChoice == 1:
        chand = paper
        status = "Lost"
    else:
        chand = scissors
        status = "Won"
elif choice == "1":
    phand = paper
    if randChoice == 0:
        chand = rock
        status = "Won"
    elif randChoice == 1:
        chand = paper
        status = "Tied"
    else:
        chand = scissors
        status ="Lost"
else:
    phand = scissors
    if randChoice == 0:
        chand = rock
        status = "Lost"
    elif randChoice == 1:
        chand = paper
        status = "Won"
    else:
        chand = scissors
        status = "Tied"
print("You chose: \n", phand)
print("Computer chose: \n", chand)
print("You ", status)
