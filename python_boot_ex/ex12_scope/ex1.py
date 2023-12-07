# 변수 범위(지역, 전역)
"""
아래 예제를 통해 지역변수와 전역변수의 차이점을 확인할 수 있다.
increase_enemies 함수 내에 있는 enemies 변수값은 함수 내에서만 유효하고
함수 외부에서는 다시 전역변수 값으로 돌아간다.
"""
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
# print(potion_strength)

# Global Scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()
