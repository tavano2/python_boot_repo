

# 데이터형식과 함수에 대해

# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

# 위 형식에도 똑같이 TypeError가 발생한다.
# 파이선은 자바와 다르게 + 연산자로 타입을 일치시켜주지 않으며
# print 함수에서는 문자형 args만 받고 있기에 변환하여 사용해야한다.

# 해당 변수의 타입을 확인하기 위해 type() 함수를 사용한다.
# print(type(num_char)) # <- <class 'int'>

# 타입 컨버전 방법
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# code Challenges
# 두 자리 숫자의 자릿수를 더하는 프로그램 작성
"""
내가 쓴 정답
inp_num = input("Please Enter Two Digit")
a = int(inp_num[0])
b = int(inp_num[1])
print(a + b)
"""

# 솔루션 정답
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# add the two integers together
two_digit_number = first_digit + second_digit
print(two_digit_number)



