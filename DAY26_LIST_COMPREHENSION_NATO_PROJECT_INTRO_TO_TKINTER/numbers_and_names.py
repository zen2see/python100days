# Create a list of numbers
def define_numbers():
    numbers = [1, 2 ,3]
    return numbers 

# PRINT WHAT IS RECEIVED (NUMBERS) IN THE FUNCTION
def lc_numbers(numbers):
    print("Some numbers:", numbers)

# ADD 1 TO EACH NUMBER 
def add_one(numbers):
    plusone = []
    # for num in numbers:
    #     plusone.append(num + 1)
    # return plusone
    return [num + 1 for num in numbers]

# GET AND PRINT LETTERS OF A NAME
def anameToLetters(a_name):
    letters_list = [letter for letter in a_name]
    print("Letters list:", letters_list)

# CONDITIONAL LIST COMPREHENSION - new_list = [new_item for item in list if test] 
def names():
    names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
    return names

def short_names():
    short_names = [name for name in names() if len(name) < 5]
    return short_names

def long_name():
    long_names = [name for name in names() if len(name) > 5]
    return long_names

def capitalize_long_names():
    cap_long_names = [name.upper() for name in names() if len(name) > 6]
    return cap_long_names
# DOUBLE A RANGE
def doubled_range():
    double_range = [x*2 for x in range(1,5)]
    return double_range

# SQUARE A RANGE
def squared_range():
    numbers2sq = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [x**2 for x in numbers2sq]
    return squared_numbers

# FILTER EVEN NUMBERS FROM A STRING OF NUMBERS
def filter_even_numbers():
    list_of_string_numbers = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    numbers = [int(strnum) for strnum in list_of_string_numbers]
    evens = [num for num in numbers if num % 2 == 0]
    return evens

# READ FILES AND CONVERT THEM TO NUMBERS
def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping non-integer value: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return numbers

# FINDING COMMON NUMBERS IN TWO DIFFERENT FILES
def find_common_numbers(file1_path, file2_path):
    file1_numbers = read_numbers_from_file(file1_path)
    file2_numbers = read_numbers_from_file(file2_path)
    common_numbers = [num for num in file1_numbers if num in file2_numbers]
    return common_numbers

# def find_common_txt(file1, file2):
#     try:
#         with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#             file1_lines = file1.read().splitlines()
#             file2_lines = file2.read().splitlines()
#         common_lines = [line for line in file1_lines if line in file2_lines]
#         return common_lines
#     except FileNotFoundError:
#         return "One or both files not found."

# MAIN FUNCTION   
def main():
    numbs = define_numbers()
    lc_numbers(numbs)
    numbs_plusone = add_one(numbs)
    lc_numbers(numbs_plusone)
    anameToLetters("Angela")
    print(doubled_range())
    print(short_names())
    print(capitalize_long_names())
    print(squared_range())
    print(filter_even_numbers())
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'
    # print(find_common_txt(file_path1, file_path2))
    common_numbers = find_common_numbers(file_path1, file_path2)
    print("Common numbers:", common_numbers)

# RUN THE PROGRAM MAIN
if __name__ == '__main__':
    main()
    