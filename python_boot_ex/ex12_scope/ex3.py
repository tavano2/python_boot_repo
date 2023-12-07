# 전역 변수를 수정하려면?
# Modifying Global Scope
enemies = 1


# def increase_enemies():
#     # 파이선에서는 지역내에서 전역 변수를 지정할 수 있다.
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# 혹은 반환문으로도 전역 변수 수정이 가능하다
def increase_enemies():
    # 파이선에서는 지역내에서 전역 변수를 지정할 수 있다.
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

"""
강의자는 전역 변수를 활용할 때는 굉장히 조심히 다뤄야한다고 이야기한다.
코드의 전체 부분에서 사용할 수 있고 
해당 지역마다 그 변수를 만들었을 때와는 별개로 수정이 가능하기 때문이다.
되도록이면 전역 변수는 상수로 지정하자.

파이썬의 전역 변수(상수) 명명 규칙은 변수 이름을 모두 대문자로 변경하는 것이다.
"""

