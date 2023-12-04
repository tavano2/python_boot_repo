# doc string
"""
지금까지 주석 대용으로도 사용했지만
사실 해당 주석 문법은 작은 문서를 만드는 문법이다
함수와 기타 코드 블록으로 코드를 작성할 때 적용할 수 있다.
하지만 공식 문서에서는 docString을 여러 라인 주석으로 쓰라고 권장하지 않기에
실무에서 사용할때는 컨트롤 + / 로 # 구문을 사용하자
"""


def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return th title case version of the name."""

    # 위와 같은 문법으로 docString을 만들 수 있다.
    if f_name == "" or l_name == "":
        return "Hey, please input your name"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? ")
                  , input("What is your last name? ")))