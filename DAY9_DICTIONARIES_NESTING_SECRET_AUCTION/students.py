student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for key,value in student_scores.items():
    # Compare value
    # print(student_scores.keys())
    # print(student_scores.values())
    # print(key)
    # print(student_scores[key])
    if student_scores[key] >= 91:
        student_grades[key] = "Outsanding"
    elif student_scores[key] >= 81 < 91:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] < 81:
        student_grades[key] = "Acceptable"
print(student_grades)