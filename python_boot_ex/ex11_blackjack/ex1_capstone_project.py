from ex1_logo import logo
from replit import clear
import random

# 나는 기존 솔루션과 다르게 만들었다.
# 기존 솔루션은 card arr를 pop하지 않고 모두 동일한 확률로 뽑히며
# 에이스카드를 1 or 11이 아닌 11로 고정했다.


def choice_value_a():
    return int(input("Ah, You get A card. you pick 1 or 11 value. what's you're choice?: "))


def append_card(arr_name, blackjack_card):
    append_val = random.choice(blackjack_card)
    blackjack_card.remove(append_val)
    arr_name.append(append_val)


def cal_user_cards(user_arr, a_value):
    user = 0
    a_value_cpu = False
    for us_item in user_arr:
        if us_item == 'J' or us_item == 'K' or us_item == 'Q':
            user += 10
        elif us_item == 'A':
            user += a_value
        else:
            user += int(us_item)
    return user


def cal_cpu_cards(cpu_arr, first_chk):
    cpu = 0
    for cpu_item in cpu_arr:
        if cpu_item == 'J' or cpu_item == 'K' or cpu_item == 'Q':
            cpu += 10
        elif cpu_item == 'A' and first_chk:
            cpu += 11
        elif cpu_item == 'A' and not first_chk:
            cpu += 1
        else:
            cpu += int(cpu_item)
    return cpu


def print_fn(my_card_arr, cpu_cards_arr, my_rs, cpu_rs):
    print(f"Your cards : {my_card_arr}")
    print(f"CPU cards : {cpu_cards_arr}")
    print(f"You : {my_rs} Cpu: {cpu_rs}")


def black_jack(cmd):
    print(cmd)
    if cmd == 'y':
        clear()
        print(logo)
        while True:
            # 함수 전역 변수
            blackjack_card = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            a_value = 1
            my_cards = []
            cpu_cards = []
            # 총 두번의 카드 뽑기
            for i in range(0, 2):
                append_card(my_cards, blackjack_card)
                append_card(cpu_cards, blackjack_card)
            # 내 카드패 공개, a뽑을시 1,11 선택
            print(f"Your cards : {my_cards}")
            if 'A' in my_cards:
                print('진입')
                a_value = choice_value_a()
            # 두번째 카드는 비공개이므로 첫번째 cpu 카드만 공개
            print(f"Computers's first card: {cpu_cards[0]}")
            # 유저가 판단하여 한장 더 뽑을시 user_arr에 한장 추가, a뽑을시 1,11 선택
            more_chance = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if more_chance == 'y':
                append_card(my_cards, blackjack_card)
                if 'A' in my_cards:
                    a_value = choice_value_a

            # 카드 모두 계산
            rs_user = cal_user_cards(my_cards, a_value)
            rs_cpu = cal_cpu_cards(cpu_cards, True)

            # 사용자 카드 합이 21이 넘을시(버스트)
            if rs_user > 21:
                print_fn(my_cards, cpu_cards, rs_user, rs_cpu)
                if input("11 You lose. Try again? enter 'y' or 'n': ").lower() == 'y':
                    black_jack('y')
                else:
                    break

            while rs_cpu < 17:
                append_card(cpu_cards, blackjack_card)
                rs_cpu = cal_cpu_cards(cpu_cards, False)
                if rs_cpu > 17 and rs_cpu <= 21:
                    break
            # cpu 카드 합이 21 넘을시(버스트)
            if rs_cpu > 21:
                print_fn(my_cards, cpu_cards, rs_user, rs_cpu)
                if input("22 You Win. Try again? enter 'y' or 'n': ").lower() == 'y':
                    black_jack('y')
                else:
                    break

            # 최종 결과
            print_fn(my_cards, cpu_cards, rs_user, rs_cpu)
            if rs_user - rs_cpu == 0:
                rs_print = 'Draw.'
            elif rs_user - rs_cpu > 0:
                rs_print = 'You Win.'
                print('')
            else:
                rs_print = 'You lose.'

            if input(f"33 {rs_print} Try again? enter 'y' or 'n': ").lower() == 'y':
                black_jack('y')

            break


if __name__ == '__main__':
    game_cmd = input("Do you want to play a game blackjack? Type 'y' or 'n': ").lower()
    black_jack(game_cmd)





