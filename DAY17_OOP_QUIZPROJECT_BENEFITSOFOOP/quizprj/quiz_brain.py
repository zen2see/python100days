from os import system

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.question_list_max = len(self.question_list)
        self.score = 0

    def more_questions(self): 
        return self.question_number < len(self.question_list)  
      
    def askq(self):
        if self.more_questions():
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q{self.question_number + 1}: {current_question.text} (True/False): ").lower()
            return user_answer
        else:
            print("No more questions available.")
            return None
    
    def the_answer(self):
        if self.more_questions():
            theanswer = self.question_list[self.question_number].answer.lower()
            return theanswer
    
    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The correct answer is: {self.the_answer()}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
    
    
    