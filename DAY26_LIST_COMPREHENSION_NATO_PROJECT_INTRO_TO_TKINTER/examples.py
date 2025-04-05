import pandas

# ITERATE THROUGH DATAFRAMES
student_dict = { "student": ["Angela", "James", "Lily"], "score": [56,76,98] }

# LOOP THROUGH A DICTIONARY
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# LOOP THROUGH A DATAFRAME
for (key, value) in student_dict.items():
    print(value)

# LOOP THROUGH ROW OF A DATAFRAME
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student =="Angela": 
        print(row.score)

# CREATE A DICTIONARY IN THIS FORMAT:
# {"A": "Alfa", "B": "Bravo"}

cap_letter_dict = {}
# CREATE A LIST OF THE PHONETIC CODE WORDS
# FROM A WPRD TJAT THE USER INPUTS
