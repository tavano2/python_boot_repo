# debug 연습1

"""
버그 원문

number = int(input())

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

"""

number = int(input())

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# 정답 if절에 == 가 아닌 = 로 작성되어 있었다.
