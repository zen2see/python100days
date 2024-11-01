print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total = round((bill * (tip/100) + bill), 2)
eachtip = round((bill * (tip/100) + bill)/5, 2)
print(f"Total bill is ${total},\
       Each person should pay  ${eachtip}")