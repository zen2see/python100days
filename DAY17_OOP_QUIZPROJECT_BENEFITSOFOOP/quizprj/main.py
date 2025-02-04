from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system, name
import time



# Clear function
def clear():
    """ CLear the screen. """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    # Create Question format
    question_bank = [Question(q["text"], q["answer"]) for q in question_data]
    # Create an instance of the QuizBrain class
    quiz = QuizBrain(question_bank)
    while quiz.more_questions():
        user_response = quiz.askq() 
        print("Your response: ", user_response)
        quiz.check_answer(user_response, quiz.the_answer())  
        print("\nPress Enter to continue...")
        quiz.question_number +=1
        input()
        clear()
    time.sleep(2)    
    clear()
    print("Good game. Thank you! Goodbye...")
    time.sleep(2)

if __name__ == '__main__':
    main()