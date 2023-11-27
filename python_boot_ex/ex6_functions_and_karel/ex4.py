"""
The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation
63번 정답
def turn_right():
    for i in  range(0, 3):
        turn_left()

def move_fn():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

while not at_goal():
    move_fn()
    while front_is_clear() and not at_goal():
        move()

"""