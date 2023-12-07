from ex4_logo import logo
import random

"""
솔루션과 나의 정답의 차이는
솔루션은 함수를 사용하여 반환값으로 게임을 종료,진행시켰다.
"""


EASY_GAME_LIFE = 10
HARD_GAME_LIFE = 5


def try_message(msg):
    return input(f"You {msg} The answer aws {result_num} Try again? Type 'yes' or 'no': ")


def chk_answer(answer, result, life_num):
    rs_val = ""
    if answer == result:
        rs_val = "success"
    elif answer > result:
        rs_val = "Too high."
        print("Too high.")
        life_num -= 1
    elif answer < result:
        rs_val = "Too low."
        life_num -= 1
    return rs_val, life_num


game_con = True
while game_con:
    print(logo)
    print("Welcome to the Number  Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        life = EASY_GAME_LIFE
    else:
        life = HARD_GAME_LIFE

    result_num = random.randint(1, 100)
    while life > 0:
        print(f"You have {life} attempts remaining to guess the number.")
        answer_num = int(input("Make a guess: "))
        print_val, life = chk_answer(answer_num, result_num, life)
        if print_val == "success":
            break
        else:
            print(print_val)

    if life == 0:
        try_ag = try_message("lose..")
    else:
        try_ag = try_message("got it!")

    if try_ag == "no":
        game_con = False

