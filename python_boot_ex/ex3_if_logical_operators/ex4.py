# code Challenges
"""
bmi 등급표
18.5 미만 저체중
18.5~25 정상체중
25~30
30~35
35 초과
"""
height = float(input())
weight = float(input())

bmi = weight / (height * height)
bmiCode = ''

if bmi <= 18.5:
    bmiCode = 'Under Weight'
elif bmi <= 25:
    bmiCode = 'Nomal Weight'
elif bmi <= 30:
    bmiCode = 'Over Weight'
elif bmi <= 35:
    bmiCode = 'Obese'
else:
    bmiCode = 'Cinically Obese'

print(f'Your BMI in {bmi}. you are allghtly {bmiCode}')

# 솔루션에서는 bimCode 변수로 넣기 보다
# 각 elif 마다 print문을 추가하여서 보여줬다.
