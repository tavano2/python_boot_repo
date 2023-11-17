# if문에 논리 연산자를 넣으면?

"""
if condition 1 & condition2 & condition3:
    do this
else
    do this
"""

"""
논리연산자 Logical Operators
A AND B ==> and 연산자
C OR D ==> or 연산자
NOT E ==> not 연산자
"""

# 롤러코스터 티켓팅 프로그램에서
# 중년 위기 ( 45 ~ 55 )세의 티켓 값을 0으로 설정하자.

print('Welcome to the Roller Coaster!')
height = int(input('What is your height in cm? '))
total_price = 0

if height >= 120:
    print('You can ride the Roller Coaster!')
    age = int(input("What is your age? "))
    if age < 12:
        print('Child tickets $5.')
        total_price += 5
    elif age <= 18:
        print('Youth tickets $7.')
        total_price += 7
    else:
        if 45 <= age <= 55:
            print('Free ticktes')
            total_price = 0
        else:
            print('Adult tickets pay $12.')
            total_price += 12

    wants_photo = input("Do You want a phto taken? Y or N. ")

    if wants_photo == 'Y':
        total_price += 3

    print(f'Your final bill is {total_price}$')

else:
    print("You can't ride the Roller Coaster!")