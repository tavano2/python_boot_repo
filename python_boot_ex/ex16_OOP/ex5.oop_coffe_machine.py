from ex5_menu import Menu, MenuItem
from ex5_coffee_maker import CoffeeMaker
from ex5_money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

program = True


def make_coffee(coffee):
    print("Make Coffee Process")
    # 원재료 충분 한지 체크
    order_item = menu.find_drink(coffee)

    enough_rs = maker.is_resource_sufficient(order_item)
    if not enough_rs:
        return

    # 동전 삽업, 처리 기능 시작
    if not money.make_payment(order_item.cost):
        return

    # 커피 제조 기능 시작
    maker.make_coffee(order_item)

    # return
    return


def machine():
    while program:
        order_input = input(f"What would you like? ({menu.get_items()}): ").lower()
        # 프로그램 동작 off
        if order_input == "off":
            return
        elif order_input == "report":
            maker.report()
            money.report()
        elif order_input == "clear":
            maker.clear()
        elif order_input == "espresso" or order_input == "latte" or order_input == "cappuccino":
            make_coffee(order_input)
        else:
            print("Sorry this is not command. try again")


machine()


"""
이처럼 15일에 개발한 프로그램보다 훨씬 가벼운 코드를 작성 가능하며
세부 내용 (커피가 어떻게 만들어지는지, 자판기가 어떻게 동작하는지)을 몰라도
메소드명만 봐도 이것이 어떤 동작을 하는지 이해할 수 있다.
"""