# code Challenges
# 주어진 점수 딕셔너리로 학생 성적 딕셔너리 만들기
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Herimione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grade = {}
for key_sc in student_scores:
    if student_scores[key_sc] > 90:
        grade = "Outstading"
    elif student_scores[key_sc] > 80:
        grade = "Exceeds Expectations"
    elif student_scores[key_sc] > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grade[key_sc] = grade

print(student_grade)
