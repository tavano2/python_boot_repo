# dictionary comprehension

# new_dict = {new_key:new_value for item in list}
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
passed_student = {key: value for (key, value) in students_scores.items() if value > 60}
print(passed_student)
