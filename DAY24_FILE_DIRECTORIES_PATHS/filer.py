# Access Windows paths on a Unix machine (or vice versa) - use pure classes
from pathlib import Path
p = Path('.')
import math
"""
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
** Delete a File
import os
os.remove("demofile.txt")
** Check if File exist:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
** Delete Folder
import os
os.rmdir("myfolder")

Absolute - relative to your root directory
Relative - relative to your current directory
"""
def main():
    # Because "r" for read, and "t" for text are the default values, you do not need to specify them.
    # Open a file on a different location:
    # f = open("D:\\myfiles\welcome.txt", "r")
    file = open("my_file.txt")
    print(file.read())
    contents = file.read()
    print(f"Contents of the file again:, {contents}")
    # By default the read() method returns the whole text, 
    # but you can also specify how many characters you want to return:
    file = open("my_file.txt", "r")
    print(file.read(6))
    # You can return one line by using the readline() method:
    file = open("my_file.txt", "r")
    print(file.readline())
    # It is a good practice to always close the file when you are done with it.
    file.close()
    # FORMATTED STRING LITERALS
    # Passing an integer after the ':' will cause that field to be a minimum 
    # number of characters wide. This is useful for making columns line up.
    print(f'The value of pi is approximately {math.pi:.3f}.') 
    # The value of pi is approximately 3.142.
    # Passing an integer after the ':' will cause that field to be a minimum number 
    # of characters wide. This is useful for making columns line up.
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
      print(f'{name:10} ==> {phone:10d}')
    # Other modifiers can be used to convert the value before it is formatted. 
    # '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
    animals = 'eels'
    print(f'My hovercraft is full of {animals}.')
    # My hovercraft is full of 'eels'.
    print(f'My hovercraft is full of {animals!r}.')
    # My hovercraft is full of 'eels'.
    # The = specifier can be used to expand an expression to the text of the expression, 
    # an equal sign, then the representation of the evaluated expression:
    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f"Debugging {bugs=} {count=} {area=}")
    # Debugging bugs='roaches' count=13 area='living room' 

    # The String format() Method
    print('We are the {} who say "{}!"'.format('knights', 'Ni')) # We are the knights who say "Ni!"
    print('{0} and {1}'.format('spam', 'eggs')) # spam and eggs
    print('{1} and {0}'.format('spam', 'eggs')) # egss and spam
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    # This spam is absolutely horrible.
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
    # The story of Bill, Manfred, and Georg.
    """
    If you have a really long format string that you don’t want to split up, it would be nice if you 
    could reference the variables to be formatted by name instead of by position. This can be done by 
    simply passing the dict and using square brackets '[]' to access the keys.
    """
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table)) # OR
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
    # Jack: 4098; Sjoerd: 4127; Dcab: 8637678  

    for x in range(1, 11):
      print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    """
    (Note that the one space between each column was added by the way print() works: 
    it always adds spaces between its arguments.)
    1   1    1
    2   4    8
    3   9   27
    ...,
    """
    




if __name__ == '__main__':
    main()