# 사랑 계산기
# code Challenges
import re

print('The Love Calculator is calculating your score...')
name1 = input()
name2 = input()

"""
NAME1에는 TRUE가 각각 몇개 들어가는지 계산
NAME2에는 LOVE가 각각 몇개 들어가는지 계산
10미만 90초과 -> Your score is X, You go together like coke and mentos
40~50점 -> Your score is Y, You are alright together
else거나 20~40, 50~90 -> 점수만 공개 
"""

str1 = ['T', 'R', 'U', 'E']
str2 = ['L', 'O', 'V', 'E']

str1_num = 0
str2_num = 0

for str_chk in str1:
    for a in re.finditer(str_chk, name1.upper()):
        if a.start():
            str1_num += 1
    for b in re.finditer(str_chk, name2.upper()):
        if b.start():
            str1_num += 1

for str_chk2 in str2:
    for a in re.finditer(str_chk2, name1.upper()):
        if a.start():
            str2_num += 1
    for b in re.finditer(str_chk2, name2.upper()):
        if b.start():
            str2_num += 1

result = int(str(str1_num) + str(str2_num))
print(result)

if 10 < result and result > 90:
    print(f'Your score is {result}, You go together like coke and mentos')
elif 40 <= result <= 50:
    print(f'Your score is {result}, You are alright together')
else:
    print(f'Your score is {result}')
