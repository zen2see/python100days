def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n2 - n1

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = float(input("What is the first number? "))
for symbol in operations:
    print(symbol)
num2 = float(input("What is the second number? "))
op = input("Pick an operation: ")
print(operations[op](4, 8))
