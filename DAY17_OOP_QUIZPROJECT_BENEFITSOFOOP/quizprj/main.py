from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import sys

question_bank = [Question(q["text"], q["answer"]) for q in question_data]
qlength = len(question_bank)

# Create an instance of the QuizBrain class
quiz = QuizBrain(question_bank)

def main():
    qnum = quiz.question_number
    # nextq = True
    while qnum < 3:
        user_response = quiz.askq()   
        print(f"Your answer: {user_response}") 
        qnum = quiz.question_number
    sys.exit()
        
if __name__ == '__main__':
    main()