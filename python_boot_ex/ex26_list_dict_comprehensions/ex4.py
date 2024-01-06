# 딕셔너리 컴프리헨션 챌린지 1

sentence = input().split(" ")

result = {item: len(item) for item in sentence}
print(result)

# 딕셔너리 컴프리헨션 챌린지 2
weather_c = eval(input())
print(weather_c)
# {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# (섭씨 x 9 / 5) + 32
weather_f = {key: (value * 9 / 5) + 32 for key,value in weather_c.items()}
print(weather_f)
