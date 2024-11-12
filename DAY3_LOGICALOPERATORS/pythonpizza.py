print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
extra_cheese = input("Do you want extra cheese? Y or N: ")
# Add extra cheese for any size pizza (Y or N): +$1
bill=0
if extra_cheese.upper() == "Y":
    bill += 1
if pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 17
    elif size.upper() == "M":
        bill += 23
    else:
        bill += 28
else:
    if size.upper() == "S":
        bill += 15
    elif size.upper() == "M":
        bill += 20
    else:
        bill += 25
print(f"Your final bill is: ${bill}.")
