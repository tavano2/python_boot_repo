# 윤년 구하기
# code Challenges
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year')
        else:
            print('Not Leap Year')
    else:
        print('Leap Year')
else:
    print('Not Leap Year')

# 솔루션과 정답이 같다.