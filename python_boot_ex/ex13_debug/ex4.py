# debug 연습 3
"""
문제 유형
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])


"""


target = int(input())
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 답안
# 1. 첫번째 if문에 or이 아닌 and 조건 변경
# 2. if 문을 나눠놓아 출력으로 인해 3,5가 함께 나눠지는 숫자일 때 여러번 출력되므로 elif로 변경
