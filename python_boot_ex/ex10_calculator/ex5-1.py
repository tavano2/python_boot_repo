# 출력문과 반환의 차이

def add(n1, n2):
    return n1 + n2


num1 = 1
num2 = 2
first_answer = add(num1, num2)

print(f"{num1} + {num2} = {first_answer}")

num3 = 3
# add(add(num1, num2), num3)
second_answer = add(first_answer, num3)

print(f"{first_answer} + {num3} = {second_answer}")

# 위와 같이 함수에 반환이 있기에 해당 반환값을 또 다른 함수 입력 값으로 사용할 수 있다
# 만일 반환값을 print문과 같이 출력한다면 해당 값은 입력 값으로 사용할 수 없다.
# 이와 같은 개념은 재귀호출할 때도 유용하게 쓰이므로 기억하자.
