result = float(input("Enter a number: "))
answer = ""
if round(result) % 2 > 0:
    answer = "Odd"
else:
    answer = "Even"
print("The number is " + answer)
