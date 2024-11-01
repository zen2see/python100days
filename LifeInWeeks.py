import sys
# Live in Weeks

age = input("What is your age: ")
def life_in_weeks(age):
    weeksLeft = (90 - int(age)) * 52
    print(f"You have {weeksLeft} weeks left.")
def main():
    life_in_weeks(age)
if __name__ == '__main__':
    sys.exit(main())  