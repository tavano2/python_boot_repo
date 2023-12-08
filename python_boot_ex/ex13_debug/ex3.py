# debug 연습 2

"""
버그 원문
year = input()

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap Year")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

"""

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap Year")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# input에 int형으로 변경하여야 한다. 문자열로 입력 받았기 때문에 진행이 불가능한 버그