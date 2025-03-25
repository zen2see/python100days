import time
import random
import re # Regular Expressions
# Access Windows paths on a Unix machine (or vice versa) - use pure classes
from pathlib import Path
p = Path('.')


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #f = open("demofile.txt", "r")  print(f.readlines())
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    # txt = "I like bananas" x = txt.replace("bananas", "apples") print(x)
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        #txt = "     banana     " x = txt.strip() print("of all fruits", x, "is my favorite")

# Return the number of bytes of a string
def byte_size(s):
    return len(s.encode('utf-8'))
    
# Read the letter file
def read_letter():
    with open('starting_letter.txt', 'r') as file:
        letter_content = file.read()
    return letter_content

# Read the list of names file
def read_names():
    with open('invited_names.txt', 'r') as name_file:
        names_list = name_file.read().splitlines()
    return names_list

# Create the "ReadyToSend" directory if it doesn't exist
def create_dir():
    Path("ReadyToSend").mkdir(exist_ok=True)

# Replace the names    
def replace_name(text, name):
    # Regular expression pattern to match "[name]"
    pattern = r"\[name\]"
    replaced_text = re.sub(pattern, name, text)
    return replaced_text

# Generate letters for each name
def generate_letters():
    # Read the content of the starting letter
    letter_content = read_letter()
    # Read the list of names from the file
    names_list = read_names()

    # create dir
    create_dir()

    for name in names_list:
        personalized_letter = replace_name(letter_content, name)
        # Save the personalized letter to a new file in the "ReadyToSend" folder
        with open(f'ReadyToSend/letter_for_{name}.txt', 'w') as output_file:
            output_file.write(personalized_letter)

def main():
    generate_letters()    

if __name__ == '__main__':
    main()