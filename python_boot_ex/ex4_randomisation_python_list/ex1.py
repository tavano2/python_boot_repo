# random module
# 우리가 개발하는 프로그램에 무작위성을 부여하려면 어떻게 해야할까?
import random
import ex1_my_module

random_integer = random.randint(1, 10)
print(random_integer)

# 이와 같이 랜덤 모듈을 사용하면 된다.
"""
여기서 모듈이라는 개념을 공부하는데, 모듈이란 정확하게 뭘까?
먼저 지금까지 대부분의 경우 코드를 스트립트 스타일의 한 페이지에 작성했다.
하지만 복잡한 것을 개발하기 위해 코드가 너무 길어지는 경우에는
코드가 너무 방대해 어떤 것이 진행되고 있는지 파악하기 힘들다.
이럴때 코드들을 개별 모듈로 나누는 작업을 하게 되며
각 모듈은 프로그램에서 서로 다른 기능을 담당하게 된다.
"""

print(ex1_my_module.pi)

"""
위와 같이 새로운 py파일에 기능을 작성하고, 사용하고 싶은 py 파일에 import 후
각 참조 영역에 접근하여 사용 가능하다.
다시 random module 공부로 돌아가자.
"""

"""
random.random() -> 0.0~1.0 사이의 부동 소수점 난수 반환 (1은 반환되지 x)
"""
print('********************')
# 0.00000 - 0.999999 ...
random_float = random.random()
print(random_float)
# 다음은 0에서 5사이의 랜덤 난수를 어떻게 실행할지 생각해보자.
# 0.00000 - 4.999999 ...
random_ex = random_float * 5
print(random_ex)
print('********************')

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

