#weight = 85
#height = 1.85
# lb = .454 kg
# foot = .3048 meter 
weight = float(input("What is your weight in kg? "))
height = float(input("What is your height meters "))
div = (weight/height)
# Calculate the bmi using weight and height.
bmi = (weight/height**2)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
