import random

# LIST OF NAMES
names  = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# DICTIONARY OF SCORES {key:value}
student_scores = {student:random.randint(1, 100) for student in names}

# DICTIONARY COMPREHENSION DICTIONARY USES --> {} LIST USE --> []
# passed_scores = {new_key:new_value for (key, value) in dictionary.items()}

def passed_students(student_scores):
    passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
    return passed_students

def top_scores(student_scores):
    high_scores = [{student, score} for (student,score) in student_scores.items() if score > 70]
    return high_scores

def main():
    print(student_scores)
    print(f"Passed students: {passed_students(student_scores)}")
    print(f"\nTop Scores: {top_scores(student_scores)}")

if __name__ == '__main__':
    main()