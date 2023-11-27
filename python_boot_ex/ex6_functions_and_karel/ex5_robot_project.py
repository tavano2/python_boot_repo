"""
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

url
https://reeborg.ca/reeborg.html?
lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""

"""
나의 정답
def turn_right():
    for i in  range(0, 3):
        turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and not wall_in_front():
        move()
    else:
        turn_left()
"""

"""
솔루션 1차 정답
def turn_right():
    for i in  range(0, 3):
        turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

1차 정답대로 진행하면 무한루프 빠지는 구간이 있다
(4면 다 우측 방향이 뚫린 경우)
해당 fix 코드는 이렇다.

def turn_right():
    for i in  range(0, 3):
        turn_left()

while front_is_clear():
    move()
turn_left()   

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and not wall_in_front():
        move()
    else:
        turn_left()
        
바로 로봇 기준으로 우측벽이 무조건 있게끔 만드는 방법이다.
"""