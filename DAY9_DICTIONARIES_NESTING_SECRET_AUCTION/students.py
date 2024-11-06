student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for key in student_scores:
    # Compare value
    print(key)
    print(student_scores[key])
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 81 >= student_scores[key]:
        student_grades[key] = "Exceeds Expectations"
        print(student_grades)
    elif 71 >= student_scores[key]:
        student_grades[key] = "Acceptable"
print(student_grades)