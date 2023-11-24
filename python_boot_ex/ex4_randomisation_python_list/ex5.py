# indexError란?
states_of_america = ["Delaware", "Pennsylvania"]
print(len(states_of_america))
# 정상 출력
print(states_of_america[1])
# indexError 출력
# print(states_of_america[2])

"""
프로그래밍을 하다 보면 종종 1~2개의 주솟값 차이로 에러가 발생하는데
이를 off-by-one 에러라고 이야기한다.
"""

# ex2
dirty_dozen = ["딸기", "사과", "바나나", "키위", "상추"]

fruits = ["딸기", "사과", "바나나", "키위"]
vegetables = ["상추"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)