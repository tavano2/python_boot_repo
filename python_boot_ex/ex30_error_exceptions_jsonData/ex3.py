# ["Apple", "Pear", "Orange"]
fruits = eval(input())


def make_pie(index):
    try:
        fruit = fruits[index]
        # print(fruit + " pie")
    except IndexError:
        print("Fruit pie")
    # 솔루션 정답에는 성공시 print문을 else 예약어로 옮겼다.
    else:
        print(fruit + " pie")


make_pie(4)
