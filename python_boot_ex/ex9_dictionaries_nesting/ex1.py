"""
파이선 딕셔너리는 실제 사전과 비슷하게 동작한다.
키 : 값으로 구성되어 있으며
키는 사전의 단어, 값은 사전에서 단어의 정의라고 생각하자.
{Key: Value}
"""

# 표준적인 딕셔너리 선언
# 맨 마지막 키에도 ,를 붙이는 것도 좋은 습관이다.
programming_dict = {
    "Bug": "An error ing a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing somthing over and over again"
}

# list[0]..[n]
# dict 호출
# print(programming_dict["Bug"])

"""
딕셔너리를 호출할 때는 키를 정확하게 입력해야한다.
정말 자주 일어나는 에러중 하나가 딕셔너리에서 값을 불러올 때
단순한 오타 때문에 일어난다. (KeyError)
그 다음은 딕셔너리에 지정한 키타입에 맞게 호출해야한다.
당연한 이야기지만 한번 더 복습하고 넘어가자.
"""

# 딕셔너리 값 추가
programming_dict["Loop2"] = "Loop2 Test"
print(programming_dict)
# 빈 딕셔너리 만들기 (리스트와 같이 코드를 처음 시작할때 초기화 해놓으면 편하다.)
empty_dict = {}
# 딕셔너리 비우기
# programming_dict = {}
# print(programming_dict)
# 딕셔너리 값 수정하기
programming_dict["Bug"] = "A moth in your computer"
print(programming_dict)

# 딕셔너리를 반복문에서 사용하기
# dicr to for는 key만 반한한다.
for thing in programming_dict:
    print("key:: ", thing)
    print("value:: ", programming_dict[thing])
