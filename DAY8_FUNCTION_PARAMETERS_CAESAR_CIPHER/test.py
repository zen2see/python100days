# Life in Weeks

age = input("What is your age: ")
def life_in_weeks(age):
    weeksLeft = (90 - int(age)) * 52
    print(f"You have {weeksLeft} weeks left.")
life_in_weeks(age)
