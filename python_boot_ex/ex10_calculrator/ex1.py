"""
우리는 지금까지
1. 아규먼트가 없는 함수
2. 아규먼트가 있어 파라미터를 받고 파라미터에 따라 동적으로 변화하는 함수
를 배웠었다

마지막으로 출력을 할 수 있는 함수에 대해 배워보자.
"""


def my_func():
    result = 3 * 2
    return result


rs_num = my_func()
print(rs_num)


"""
출력과 관련해 함수에 대해 접근하는 방식이 거의
하나의 기계와 같다는 것을 알 수 있다.
빈 병이 들어가는 기계를 갖고 있다고 가정하면
어떤 프로세싱이나 입력 다음에는 우유를 채운 병이라는 결과가 나올 것이다.
이 경우, 이 함수가 빈 유리병이라는 입력 값을 가지고 있고
출력 값은 우유가 담긴 유리병 값을 가지게 되며
빈 유리병에서 우유가 담긴 유리병으로 제조하는 방식이 함수 내 코드라고 이해하면 되겠다.
"""


def format_name(f_name, l_name):
    format_f = f_name.title()
    format_l = l_name.title()
    return format_f + " " + format_l


full_name = input()
name_arr = full_name.split(" ")
rs_name = format_name(name_arr[0], name_arr[1])
print(rs_name)
