# for 반복문과 range 함수
# range 함수는 매우 유용하다

"""
for number in range(a, b):
    print(number)
"""
#
# for number in range(1, 10, 2):
#     print(number)

# 1부터 100까지 숫자를 모두 더하기
total = 0
for number in range(1, 100 + 1):
    total += number

print(total)

