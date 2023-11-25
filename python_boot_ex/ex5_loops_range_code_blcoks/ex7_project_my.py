# final project
# 비밀번호 생성기 프로그램
"""
내가 만든 솔루션은 첫번째 질문을 한단계 더 꼬은 것이다.
출제자의 의도는 1. 문자 몇개 2. 특문 몇개 3. 숫자 몇개를 조합한 것인데
나는 1. 총 비밀번호 길이 2. 그 중 특문 몇개 3. 그 중 숫자 몇개를 랜덤으로 생성하는
프로그램을 만들었다.

내가 오해해서 만든 정답 : ex7_project_my.py
솔루션 hard lv 정답 : ex7_proejct_solution.py
"""

import copy
import random

print('Welcome to the PyPassword Generator!')
pass_len = list(range(int(input('Please enter the total length of the password you want to set.\n'))))
symbols_len = int(input('How many symbols would you like?\n'))
num_len = int(input('How many numbers would you like?\n'))

# 랜덤 위치를 저장할 배열
sy_ran_arr = []
num_ran_arr = []

# 랜덤 위치 생성 후 비밀번호 최종 생성시 필요한 비밀번호 전체 길이
loop_len = len(pass_len)

# 할당된 위치에 무작위 값을 넣을 배열
lower = list(chr(i) for i in range(ord('a'), ord('z') + 1))
upper = list(chr(i) for i in range(ord('A'), ord('Z') + 1))
alphabet_arr = lower + upper
symbols_arr = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
num_arr = copy.deepcopy(pass_len)

# 최종 비밀번호 변수
result = ''

# 특수문자 넣을 랜덤 위치 생성
for sy_idx in range(1, symbols_len + 1):
    ran_num_sy = random.choice(pass_len)
    sy_ran_arr.append(ran_num_sy)
    pass_len.remove(ran_num_sy)

# 숫자 넣을 랜덤 위치 생성
for num_idx in range(1, num_len + 1):
    ran_num = random.choice(pass_len)
    num_ran_arr.append(ran_num)
    pass_len.remove(ran_num)

# 각 배정된 숫자 찾아 비밀번호 생성
for idx in range(0, loop_len):
    for sy_item in sy_ran_arr:
        if idx == int(sy_item):
            result += str(random.choice(symbols_arr))
    for num_item in num_ran_arr:
        if idx == int(num_item):
            result += str(random.choice(num_arr))
    for alp_item in pass_len:
        if idx == int(alp_item):
            result += str(random.choice(alphabet_arr))

# 생성된 비밀번호 출력
print(f'Here is your password: {result}')
