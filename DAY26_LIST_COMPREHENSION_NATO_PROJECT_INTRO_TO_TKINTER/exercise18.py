
# DAY 26 LIST COMPREHENSION EXERCISE 18

"""
You are going to use Dictionary Comprehension to create a dictionary called 
result that takes each word in the given sentence and calculates the number
 of letters in each word.   
"""

# A SENTENCE
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

def sentence_to_words(sentence):
    Word_list =  [word for word in sentence.split()]
    return Word_list 

def sentence_word_count(sentence):
    Word_count = {word: len(word) for word in sentence.split()}
    return Word_count

def main():
    print(sentence_to_words(sentence))
    print(sentence_word_count(sentence))

if __name__ == '__main__':
    main()