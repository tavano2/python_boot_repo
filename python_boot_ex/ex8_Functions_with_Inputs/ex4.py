# code Challenges
# 입력값이 소수인지 확인하는 함수 작성

def prime_checker(number):
    prime_len = 0
    for i in range(1, 101):
        if number % i == 0:
            prime_len += 1
    if prime_len == 2:
        print(f'This Number is prime: {number}')
    else:
        print(f'This Number is composite: {number}')


"""
솔루션 정답
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print(f'This Number is prime: {number}')
    else:
        print(f'This Number is composite: {number}')
"""


n = int(input())
prime_checker(number=n)
