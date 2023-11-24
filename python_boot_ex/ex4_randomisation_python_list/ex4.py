# code Challenges
import random

names = input("check your names: ")
nameList = names.split(", ")

"""
내 정답
ran_result = random.randint(0, len(nameList)-1)
print(f'{nameList[ran_result]} is going to buy the meal today!')
"""

# 솔루션 정답
num_items = len(nameList)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = nameList[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")



