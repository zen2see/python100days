"""
KEY                VALUE
BUG               Error in a program prevents the prog from running expectedly
FUNCTION    Piece of code that you can easily call over and over again
LOOP            The action of doing something over and over again
"""
programming_dictionary = {"Bug":"Error in a program prevents the prog from running expectedly",\
                          "Function":"Piece of code that you can easily call over and over again",\
                          }
print(programming_dictionary["Function"])
programming_dictionary["Loop"] = "The action of doing something over and over again"
empty_dictionary = {}
# Edit an item in a dictionary
programming_dictionary["Loop"] = "Repeating an action over an over again."
# Loop through a dictionary displaying keys
for thing in programming_dictionary:
    print(thing)
# Loop through a dictionary displaying keys and values
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])