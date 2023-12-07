"""
파이선과 다른 언어의 차이
조건문이나 반복문에서 초기화를 먼저 진행하지 않아도
같은 지역내일 경우 해당 변수를 사용할 수 있다.
"""

# There is no block scope
game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]


# print(new_enemy)
