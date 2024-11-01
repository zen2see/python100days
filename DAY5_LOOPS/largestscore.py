student_scores = [150, 142, 185, 120, 171, 184, 149]
student_scores.sort()
print("Highest score: ", student_scores[-1])
max_score = 0
for score in student_scores:
   if score > max_score:
     max_score = score
print("Max score is:", max_score)
