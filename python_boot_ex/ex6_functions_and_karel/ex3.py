# while loops
# 조건식에 부합할때까진 무한적으로 반복되는 문법

"""
while something_is_true
    #do something any
"""

# 이후에 로봇 동영상으로 넘어가기에 62~65 동영상도 추후 공부한다.
"""
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

1. while문을 이용한 허들 넘기 
nummber_of_hurdles = 6
while nummber_of_hurdles > 0:
    move_fn()
    nummber_of_hurdles -= 1
    print(nummber_of_hurdles)

2. while문을 이용해서 허들을 넘지만 깃발이 어디에 위치해 있을지 모름
at_goal() 함수가 true면 깃발이 위치한 것으로 판단한다.

nummber_of_hurdles = 6
while nummber_of_hurdles > 0:
    move_fn()
    nummber_of_hurdles -= 1
    if at_goal():
        break

혹은
while not at_goal():
    move_fn()

for문과 while은 어떠한 경우에 써야 가독성이 좋을까?

강사의 말로는 for 반복문의 경우 어떤 것을 반복하고
반복하는 각 아이템에 대해 뭔가를 해야 할 때 유용하다.

while문은 전체 순서에서 몇 번째에 해당하는지,
어떤 아이템을 반복할지가 아닌, 그저 특정 작업을 설정한 조건에 도달할 때까지
수없이 반복하려고 할 때 유용하다.

while문은 조건을 만족하면 무한반복 될 수 있기에 조심해야한다.
만일 왜 무한 반복이 되는지 모르겠다면, 조건식을 print로 출력해보자.
"""

"""
64번 강의 : 높낮이가 자유인 허들 넘기
def turn_right():
    for i in  range(0, 3):
        turn_left()

def move_fn():
    if wall_in_front():
        turn_left()
    task = 0
    while wall_on_right():
        move()
        task += 1
    turn_right()
    move()
    turn_right()
    while task > 0:
        move()
        task -= 1
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        move_fn()
"""
