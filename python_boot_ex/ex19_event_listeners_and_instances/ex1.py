"""
이번 강의에서는 고차 함수와 이벤트 리스너에 대해 알아보자
키보드를 눌렀을 때나 마우스를 클릭했을 때 동작하는 이벤트에 대해서
이벤트 리스너라고 부른다.
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(fun=move_forwards, key="space")

# 여기서 매우 중요한 개념이 등장한다.
# 함수를 인수로 사용할 때는 괄호를 추가하지 않는다. 이는 자바스크립트 공부에서도 배웠던 내용이다.
# 괄호를 넣으면 그 자리에서 바로 실행되기 때문이다.
# 함수의 간접 실행이라고 볼 수 있다.

screen.exitonclick()

"""
그렇다면 이벤트리스너 내부 구조는 어떻게 되어 있길래 간접 실행이 가능한걸까?
ex
def add(n1, n2):
    return n1 + n2

def cal_fn(n1, n2, func):
    return func(n1, n2)
    
이와 같은 형식으로 구성되어 있다.
이를 고차함수 개념이라고도 하며, 다른 함수와 함께 작동하는 함수를 말한다.
위 예제의 경우 cal_fn이 고차함수이다.

그리고 이와 같은 고차함수를 간접으로 호출할 때는 키워드 아규먼트를 사용하자.
"""