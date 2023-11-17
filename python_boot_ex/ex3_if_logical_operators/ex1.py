
print('hello python')
# if / esle 문 정의
# 특정 조건에 따라 a 또는 b 둘 중 하나를 실행하는 문법이다.
"""
if condition:
    do this
else:
    do this
"""
# ex
water_level = 50
if water_level > 80:
    print('Drain Water')
else:
    print('Continue')

# ex2
# 파이썬에서는 띄어쓰기와 들여쓰기가 정말 중요하다.
print('Welcome to the Roller Coaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the Roller Coaster!')
else:
    print("You can't ride the Roller Coaster!")

"""
비교 연산자
> : 초과
< : 미만
>= : 이상
<= : 이하
== : 같음
!= : 다름

처음 프로그래밍을 할 때 제일 헷갈리는것이 =과 ==인데
= : 우측 값을 왼쪽 변수에 참조하는 참조 연산자.
== : 동일 값일 때 TRUE 아니면 FALSE를 반환하는 비교 연산자.
"""



