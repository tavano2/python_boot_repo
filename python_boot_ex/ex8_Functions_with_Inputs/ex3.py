# code Challenges
import math

test_h = int(input())
test_w = int(input())
coverage = 5

"""
올림 함수 math 외부 모듈의 ceil 메소드
"""


def paint_calc(height, width, cover):
    cans = (height * width) / cover
    print(f"You'll need {math.ceil(cans)} cans of paint")


paint_calc(height=test_h, width=test_w, cover=coverage)


