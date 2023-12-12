# 커피 자판기 프로그램을 구현해보자
"""
1. 3개의 음료를 선택할 수 있음 (1. 에스프레소, 2. 라떼, 3. 카푸치노)
2. 음료들의 들어가는 재료와 가격은 당연히 다르다 (coffe_data 참고)
3. 커피 자판기에 관리자가 수시로 재료를 채워줘야 하는게 있다.
4. 동전을 넣어 작동하며 4개의 동전을 사용한다. (1, 5, 10, 25센트)
"""

# TODO 1. 현재 재료 상태 확인 기능 & 프로그램 off 기능 & 원재료 clear(추가 기능)
# TODO 2. 사용자가 커피를 주문할 때 재료가 충분한지 확인
#  - 모자를시 failed 문구와 함께 시작점으로 회귀
# TODO 3. 동전 처리 기능
#  - 모자를시 사용자가 입력한 돈을 반환해주고 시작점으로 회귀
#  - 주문 커피보다 사용자가 돈을 더 넣었을시 나머지 금액 반환
# TODO 4. 재료 충분 & 동전을 커피값 이상으로 넣었다면 커피를 만들어 제공
#  - 커피 제공 후 재료 차감
#  - 커피 제공 후 자판기 내부 금액 상승

from ex2_coffe_data import MENU, resources

CLEAR_WATER = 300
CLEAR_MILK = 200
CLEAR_COFFEE = 100

program = True
program_money = 0


# 원재료 리포트 기능
def pr_report(total_money):
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${total_money}")


# 원재료 초기화 기능
def clear_resource():
    resources["water"] = CLEAR_WATER
    resources["milk"] = CLEAR_MILK
    resources["coffee"] = CLEAR_COFFEE


# 재료 체크 기능
def chk_resource(coffee_rs, origin_rs):
    enough_rs = ""
    for item in coffee_rs:
        if coffee_rs[item] >= origin_rs[item]:
            enough_rs = item
            break
    return enough_rs


# 동전 계산 기능
def cal_cost(quarters, dimes, nickles, pennies):
    sum_quarters = round(0.25 * quarters, 2)
    sum_dimes = round(0.1 * dimes, 2)
    sum_nickles = round(0.05 * nickles, 2)
    sum_pennies = round(0.01 * pennies, 2)
    return sum_quarters + sum_dimes + sum_nickles + sum_pennies


# 0원 반환
def zero_cost():
    return 0


# 커피 작업 기능
def make_coffee(coffee):
    print("Make Coffee Process")
    # 원재료 충분 한지 체크
    coffee_resource = MENU[coffee]["ingredients"]
    coffee_cost = MENU[coffee]["cost"]

    enough_rs = chk_resource(coffee_resource, resources)
    if enough_rs != "":
        print(f"Sorry there is not enough {enough_rs}")
        return zero_cost()

    # 동전 삽입 프로세스 시작
    quarters = int(input("How Many quarters?: "))
    dimes = int(input("How Many dimes?: "))
    nickles = int(input("How Many nickles?: "))
    pennies = int(input("How Many pennies?: "))

    # 동전 처리 기능 시작
    total = cal_cost(quarters, dimes, nickles, pennies)
    if coffee_cost > total:
        print("Sorry that's not enough money. Money refunded.")
        return zero_cost()
    print(f"Here is ${total - coffee_cost} in change.")

    # 커피 제조 기능 시작
    for item in coffee_resource:
        resources[item] = resources[item] - coffee_resource[item]

    # return
    print(f"Here is your {coffee}. Enjoy!")
    return coffee_cost


# 커피 머신 기능
def machine(total_money):
    while program:
        order_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # 프로그램 동작 off
        if order_input == "off":
            return
        elif order_input == "report":
            pr_report(total_money)
        elif order_input == "clear":
            clear_resource()
        elif order_input == "espresso" or order_input == "latte" or order_input == "cappuccino":
            cost = make_coffee(order_input)
            total_money += cost
        else:
            print("Sorry this is not command. try again")


machine(program_money)
