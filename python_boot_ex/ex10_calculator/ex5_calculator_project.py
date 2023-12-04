# calculator
from ex5_calculator_art import logo


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


# 파이선에서는 아래와 같이
# 딕셔너리 안에 함수를 저장하고 해당함수를 호출하여 변수에 담아, 사용 가능하다.
cal_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator(next_num, first_chk):

    if first_chk:
        first_chk = False
        num1 = float(input("What's the first number?: "))
        for item in cal_dict:
            print(item)
    else:
        num1 = next_num

    op_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    rs_fn = cal_dict[op_symbol]
    rs_num = rs_fn(num1, num2)

    chk_val = input(f"Type 'y' to continue calculating with {rs_num}, or type 'n' to start a new calculation: ")

    if chk_val == 'n':
        rs_num = 0
        first_chk = True

    return calculator(rs_num, first_chk)


# main
print(logo)
while True:
    calculator(0, True)
