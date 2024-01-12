# handling errors & exceptions
# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_ex"]


# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

"""
우리는 위와 같은 여러 예외 상황들을 겪고 코드를 수정했다.
하지만 현실에서는 이 모든 것들을 파악하지 못하고 발생할 수 있고
미리 알 수 있는 에러들을 다른 방법으로 사용자에게 보여주거나, 처리할 수 있다.

이를 위해 예외 처리 방법을 학습히자

try: 예외를 유발할 수 있는 코드 블록을 감지하는 예약어

except: 예외가 발생하면 실행 되는 블럭 예약어

else: 예외가 없었을 때 실행 되는 예약어

finally: 어떤 일이 일어나더라도 반드시 실행되는 블럭 예약어
"""
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"That key does {error_msg} not exist.")
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # Raising Exceptions (나만의 예외 만들기)
    raise TypeError("This is an error that I made up.")
