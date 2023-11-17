
# 중첩 if / elif 문

"""
중첩 if
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
"""

"""
print('Welcome to the Roller Coaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the Roller Coaster!')
    age = int(input("What is your age? "))
    if age <= 18:
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print("You can't ride the Roller Coaster!")
"""


"""
여기서 티켓 사장이 연령별 티켓 값을 3가지 조건으로 추가하였다.
이럴 경우에는 어떤 문법을 사용해야 할까?
elif 문법을 사용하면 된다.

if condition1:
    do A
elif condition2:
    do B
else:
    do this
"""

print('Welcome to the Roller Coaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the Roller Coaster!')
    age = int(input("What is your age? "))
    if age < 12:
        print('Please pay $5.')
    elif age <= 18:
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print("You can't ride the Roller Coaster!")