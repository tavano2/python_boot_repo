# 다중 return문
"""
파이선에서 함수가 하나 이상의 리턴문을 가진 경우
무슨 일이 일어나는지 알아보자.

1. 리턴문 뒤에는 함수 내부 코드가 실행되지 않음
2. 다양한 분기문을 통해 리턴 처리를 할 수 있음 (ex 가져오는 이름 값이 없을때 유효성 처리 등등)
"""


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Hey, please input your name"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? ")
                  , input("What is your last name? ")))
