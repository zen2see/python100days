# Access Windows paths on a Unix machine (or vice versa) - use pure classes
from pathlib import Path
p = Path('.')
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
"""
def main():
    # Because "r" for read, and "t" for text are the default values, you do not need to specify them.
    # Open a file on a different location:
    # f = open("D:\\myfiles\welcome.txt", "r")
    file = open("my_file.txt")
    print(file.read())
    contents = file.read()
    print("Contents of the file again:", contents)
    # By default the read() method returns the whole text, 
    # but you can also specify how many characters you want to return:
    file = open("my_file.txt", "r")
    print(file.read(6))
    # You can return one line by using the readline() method:
    file = open("my_file.txt", "r")
    print(file.readline())
    # It is a good practice to always close the file when you are done with it.
    file.close()

if __name__ == '__main__':
    main()