import sys

def main(arg1, arg2):
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Not enough arguments provided.")