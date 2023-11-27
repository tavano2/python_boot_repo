# Indentation
# 들여쓰기

"""
파이썬에서 들여쓰기가 얼마나 중요한지 알아보자.
들여쓰기 (스페이스바 4개)
"""


def my_funtions():
    print('Hello')


print('World')

"""
위 경우에는 함수 호출하기전까지는
World만 출력되는 것을 알 수 있다.
좀 더 쉽게 이해하려면 파일 구조를 예로 들면 되는데
my function 폴더 안에 hello라는 텍스트 파일이 있고
world 텍스트 파일은 my function 폴더와 동일한 경로에 위치해 있다.
"""
sky = 'clear'


def my_funtions2():
    if sky == 'clear':
        print('blue')
    elif sky == 'cloudy':
        print('grey')
    print('Hello')


print('World')

"""
위와 같이 들여쓰기가 될 수록 다른 코드 블럭이고
이를 한번에 구분할 줄 알아야 한다.
"""