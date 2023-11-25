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

import random

# hard_lv

# 할당된 위치에 무작위 값을 넣을 배열
lower = list(chr(i) for i in range(ord('a'), ord('z') + 1))
upper = list(chr(i) for i in range(ord('A'), ord('Z') + 1))
alphabet_arr = lower + upper
symbols_arr = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
num_arr = list(range(1, 10 + 1))

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

pass_list = []
pass_rs = ''

# input에 할당한 길이만큼 비밀번호 배열에 삽입
for char in range(1, nr_letters + 1):
    pass_list.append(random.choice(alphabet_arr))
for char in range(1, nr_symbols + 1):
    pass_list.append(random.choice(symbols_arr))
for char in range(1, nr_numbers + 1):
    pass_list.append(random.choice(num_arr))
# random 외부 모듈로 섞어서 최종 결과 변수에 담기
random.shuffle(pass_list)
for item in pass_list:
    pass_rs += str(item)

print(f'Here is your password: {pass_rs}')
