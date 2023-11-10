print(int(8 / 3))

# 반올림,반내림 해보기
print(round(8 / 3, 2))
# 버림
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

# User scores a point
# 증감 차감 * / 연속 연산자
score = 0
score += 1
print(score)

# F-String
score = 1
heigth = 1.8
isWinning = True
# 각가 다른 타입을 프린팅하려면 기존의 방식으로는 매우 불편했다.
# 그래서 나온 포맷팅 방식이 F-String 방식이다.
print("your score is " + str(score))
# f-String
print(f"your score is {score}, your height is {heigth}, you are winning is {isWinning}")

# code Challenges
"""내가 쓴 정답
age = input()
all_week = 90 * 52
my_week = int(age) * 52
left_week = all_week - my_week
print(f"You have {left_week} weeks left.")
"""
# 솔루션 정답
age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")
