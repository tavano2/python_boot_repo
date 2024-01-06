# 리스트 컴프리헨션

"""
리스트 컴프리헨션이란?
    이전 리스트로부터 새로운 리스트를 만드는 경우를 말한다.
"""

# for loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# list Comprehension
new_list = [n + 1 for n in numbers]


name = "Angela"
new_list_name = [letter + " " for letter in name]
print(new_list_name)

"""
list, range, string, tuple 같은 것을 시퀀스라고 부르는데
아것들은 명확하게 순서를 가지고 있기 때문에 시퀀스라고 부른다.
그래서 리스트 컴프리헨션을 사용할 때 각 요소들이 시퀀스를 써서 순서대로 통과하게 되는 원리이다.
"""

new_num_arr = [n * 2 for n in range(1, 5)]
print(new_num_arr)

# 조건식이 추가된 컴프리헨션
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_names = [name.upper() for name in names if len(name) >= 5]
print(upper_names)


def test(nm):
    return nm.upper()


fn_names = [name for name in names if test(name)]

print(fn_names)

