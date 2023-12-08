# 버그를 찾아내는 방법과 없애는 방법
# 1. 문제를 그려보기
"""
발생한 문제가 너무 복잡하거나 스스로 이해할 수 없다면 버그를 고치는 일은 불가능하다.
그러니 실타래처럼 꼬인 문제를 풀고 이해하려 노력해보자.
"""

############DEBUGGING#####################


# Describe Problem
# 첫번째 문제는 range안에 있는 마지막 인덱스가 20을 반복하지 못하여
# 출력문이 나오지 않는 버그이므로 range를 늘렸다.
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# 2. 발견한 버그를 다시 구현해보기
"""
발생한 버그를 다시 구현하다보면 한번은 우연히 발생시키지만
다음 번에도 그러리란 보장은 없고, 지속적으로 같은 코딩에 버그가 발생한다면
해당 버그는 매우 고치리 어려울 것이다.
"""
# Reproduce the Bug
# 해당 버그는 random 모듈 실행시 list에서 index가 벗어나는 오류가 발생한다.
# 인덱스 개념을 실수한 것으로 1, 6으로 설정한 인자를 0, 5로 변경하자.
# 이런 인덱스 버그는 간혈적으로 발생하기 때문에 (1~5 랜덤 인덱스는 추출됨) 문제를 찾기 힘들다.

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6
# print(dice_imgs[dice_num])
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# 3. 컴퓨터의 입장에서 생각해보기
"""
자신이 컴퓨터라고 생각하면서 코드를 읽으면 디버깅하기 쉬워진다.
"""
# Play Computer
# 해당 버그는 1994년을 입력했을시 조건문에서 모두 FALSE가 발생하는 버그이다.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# 4. IDE나 콘솔에서 에러가 발생했을때 해당 현상 수정하기
# 들여쓰기를 하지 않아 print문에서 에러가 발생하고
# input값을 int로 변경하지 않아 두번째 에러가 발생한다.
# 마지막으로는 f스트링 문법이 아니기에 {age}밸류가 출력되지 않는다.

# Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
#
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# 5. 출력문으로 버그를 때려잡자
# 두번째 변수에 등호가 두개 들어가 input에 입력한 값이 참조되지 않아서 일어난 버그이다.
# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(pages)
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# 6. 디버거 프로그램을 활용하자
# append 시점을 for 지역이 아닌 def 지역에서 넣어서 발생한 버그이다.
# Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

"""
이외의 여러 디버깅 팁

7. 잠시 휴식하기
-> 에러나 버그가 발생했을 때 바로바로 수정하는게 베스트지만 컨디션과 몸상태에 따라
코드를 아무리 쳐다봐도 발견하지 못할 때가 있다. 가끔은 휴식을 취해주자.
8. 친구나 지인에게 조언듣기
-> 정말 나의 수준으로는 발견할 수 없을때는 나보다 잘하는 친구나 지인의 도움을 받자.
사람들은 각자의 코딩 스타일과 논리적인 가정을 하고, 이 과정에서 습득할 수 있는 부분과 해결방안을 찾을 수 있다.
9. 코드를 자주 실행하자
-> 코드의 호흡을 길게 작성하고 실행하는 것이 아닌 스텝 별로 실행하여 조각한다면
내가 놓쳤던 부분과 버그를 잡을 수 있는 확률이 높아진다.
또한 수많은 버그가 발생했을 때는 한 번에 하나씩 처리하는 것을 추천한다.
10. 스택오버플로우에 물어보자
-> 독특한 버그가 발생했을 때 오버플로우를 검색하여 문제를 해결하자.
이미 많은 선배들이 내 앞을 지나가고, 밟았으며 그들이 고민한 버그를 찾고 있을 수 있기 때문이다.
오버플로우를 마지막에 추천한 이유는 내가 직접 해결하려 노력해보는 것이 실력 향상에 도움 되기 때문이다.

마지막으로 버그를 만드는 것에 두려워 하지말자.
버그를 만드는 것이 프로그래머가 되는 길에서 가장 중요한 과정이다.
"""