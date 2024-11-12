import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = ""


final = []
solved = False
for position in range(word_length):
    placeholder += "_"
while not solved:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    display = ""
    guess = input("Guess a letter: ")
    # print(chosen_word)
    # print(word_length)
    # print(final) 
    # print(''.join(final))   
    for position in range(word_length):
        #print("position: ", position)
        #print("chosen_word[position]", chosen_word[position], "guess: " , guess)
        if chosen_word[position] == guess:
            # print("guess position", guess[position])
            final.append(guess)
            display += guess
            # print(final)
            # print(display)
        elif chosen_word[position] in final:
            display += chosen_word[position]
        else:
            display += "_ "
    print(display)        
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        print(stages[lives])
        if lives == 0:
          #print("YOU LOSE!!")
          print(f"***************IT WAS {chosen_word} YOU LOSE**********************")
          print(stages[lives])
          exit()
    if "_" not in display:
        solved = True
        #print("YOU WIN!!")
        print("****************************YOU WIN****************************")
# print(stages[lives])

