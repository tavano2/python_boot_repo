# Functions
"""
코드로 하여금 다양한 기능을 수행하게 만드는 단위
함수를 선언할 때는 반드시 괄호가 들어간다
ex) print() <-
"""
print('Hello')
num_char = len('Hello')
print(num_char)


# 나만의 함수 만들기
def my_function():
    print('Hello')
    print('Bye')


print('***************************')
# my_function의 경우 입력받는 arg가 없기에 호출할 때도 입력 값 없이 호출한다.
my_function()

# 59,60 수업 로봇 챌린지는 추후 진행
"""
챌린지는 https://reeborg.ca/reeborg.html?
lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
에서 진행한다.

59번 challenge code
def turn_right():
    turn_left()
    turn_left()
    turn_left()

정사각형 움직이기
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

60번 강의 챌린지는 https://reeborg.ca/reeborg.html?
lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
에서 진행한다.

60번 chaallenge
def turn_right():
    for i in  range(0, 3):
        turn_left()

def move_fn():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in  range(0, 6):
    move_fn()
"""

