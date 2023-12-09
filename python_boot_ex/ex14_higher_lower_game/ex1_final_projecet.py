"""
코드를 작성하기 전 해두면 좋은 습관
1. 문제를 나누어 생각하기
- 기능별로 주석을 달거나 다이어그램을 작성하자.
2. TO-DO list 작성
3. 코드를 나눠서 입력하기
4. 코드 작성 -> 실행 -> 수정
5. 한가지를 완료하면 그 다음 쉬운 작업 진행하기
"""

# 오늘의 게임 랜덤의 두 아이템을 꺼내 팔로워 수가 높을 것 같은 아이템을 선택
# 성공시 계속 이어가기
# 실패시 재도전

from ex1_art import logo, vs
from ex1_data import data
import random

FIN_LANG = len(data)
SUCCESS_MESSAGE = "OK"
FAILED_MESSAGE = "FAILED"


def get_item(data_arr, chk_val, rs_val):
    if chk_val:
        rs_type_a = random.choice(data_arr)
        data.remove(rs_type_a)
        rs_type_b = random.choice(data_arr)
        data.remove(rs_type_b)
    else:
        rs_type_a = rs_val
        rs_type_b = random.choice(data_arr)
        data.remove(rs_type_b)

    return rs_type_a, rs_type_b


def sel_follower_fn(sel_val, a_ob, b_ob):
    if sel_val == 'a':
        follower_val = a_ob['follower_count']
        sel_ob = a_ob
    else:
        follower_val = b_ob['follower_count']
        sel_ob = b_ob
    return follower_val, sel_val, sel_ob


def calc_score(sel_follower_val, sel_val, a_ob, b_ob):
    rs_string = FAILED_MESSAGE
    if sel_val == "a" and sel_follower_val > b_ob['follower_count']:
        rs_string = SUCCESS_MESSAGE
    elif sel_val == "b" and sel_follower_val > a_ob['follower_count']:
        rs_string = SUCCESS_MESSAGE

    return rs_string


def game(chk_val):
    suc_ob = {}
    suc_num = 0
    game_data = data

    while len(game_data) > 0:

        print(logo)
        if chk_val:
            val_a, val_b = get_item(game_data, chk_val, {})
        else:
            print(f"You're right! Current socre: {suc_num}.")
            val_a, val_b = get_item(game_data, chk_val, suc_ob)

        print(f"Compare A: {val_a['name']}, a {val_a['description']}, from {val_a['country']}")
        print(vs)
        print(f"Compare B: {val_b['name']}, a {val_b['description']}, from {val_b['country']}")

        sel_follower_val, sel_val, sel_ob = sel_follower_fn(input("Who has more followers? Type 'A' or 'B': ").lower(), val_a, val_b)
        result = calc_score(sel_follower_val, sel_val, val_a, val_b)

        if result == SUCCESS_MESSAGE:
            suc_num += 1
            suc_ob = sel_ob
            chk_val = False
        else:
            try_val = input(f"Sorry, that's worng Final score: {suc_num}. Try again? Type 'yes' or 'no': ").lower()
            if try_val == 'yes':
                game(True)
            else:
                return

    if suc_num == FIN_LANG - 1:
        print(f"You Complete Game! Wow! Final score: {suc_num}")


game(True)
