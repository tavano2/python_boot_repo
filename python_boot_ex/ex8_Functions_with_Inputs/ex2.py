# Functions with  morer than 1 input
# def greet_with(name, location):
#     print(f'Your name is {name}, your live in {location}')
#
#
# greet_with("Leem", "Suwon")

"""
만일 함수에서 아규먼트 값을 서로 바꾸면 어떻게 될까?
당연히 파라미터의 값도 서로 바뀐다.
보통의 프로그래밍 언어는 Positional Argument를 사용하고 있어
아규먼트의 순서를 꼭 지켜야 함을 알아두자.
"""

"""
만일 다중 아규먼트 함수를 사용할때 더 확실하게 하려면 어떻게 해야할까?
여기서 Keyword Arguments를 사용한다.
"""


def greet_with(name, location):
    print(f'Your name is {name}, your live in {location}')


# 아래와 같이 키워드를 사용하면 순서에 상관 없이 지정한 파라미터대로 값이 바인딩된다.
greet_with(location="Suwon", name="Leem")