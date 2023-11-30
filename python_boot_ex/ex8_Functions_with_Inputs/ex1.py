# Functions
def greet():
    print('Hello')
    print('World')
    print('Leem')


greet()

"""
이렇게 함수는 호출할 때 마다 함수안에 작성한 코드를 실행한다
만일 아주 약간의 부분만 변경해서 조금씩 다른 결과를 표출할 수 있게 한다면
훨씬 유용하게 사용 가능하다.
"""


def greet_with_name(name):
    print(f'Hello {name}')
    print(f'World {name }')
    print(f'Leem {name}')


greet_with_name("Leem")


"""
여기서 프로그래밍에 중요한 개념이 등장한다
내가 함수안에 넣은 "Leem"은 name이랑 동일하다
즉 name = "Leem"인데 각각 명칭을
  파라미터 = 아규먼트 라고 칭한다.
파라미터는 함수에 전달된 데이터의 이름이고
아규먼트는 그 데이터의 실제 값이다.
"""
