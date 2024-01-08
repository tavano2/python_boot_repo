# 여러 개의 인수를 취할 수 있는 함수 만들기 학습
# *args <= 참조된 파라미터들을 튜플로 구성하여 함수에서 사용한다.
def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


# **kwargs
# kwargs는 참조된 파라미터들을 딕셔너리로 구성하여 함수에서 사용한다.
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Ford", model="KHKHK")
print(my_car.model)

