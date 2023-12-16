# 직접 커스텀 클래스 만들어보기
# 빈 클래스나 함수를 만들고 싶을 때는 pass 예약어를 사용한다.
# 파이썬의 클래스명에 모든 단어의 첫번째 글자는 대문자로 작성한다. (파스칼 케이스)
# 파이썬에서 클래스명은 파스칼, 나머지는 스네이크 케이스로 작성된다 (스네이크 : 각 단어를 언더바로 분리)
# class User:
#     pass
#
#
# user = User()
# user.id = "001"
# user.username = "angela"
#
# print(user.username)

"""
클래스에서 객체를 생성할때 어떻게 시작 정보들을 편리하게 넣을 수 있을까?
위 예시대로 user가 늘어날때 마다 직접 명시한다면 굉장히 불편하고, 실수가 일어날 수 있다.
여기서 생성자 개념이 도출된다.

생성자는 도면(클래스)의 일부로, 클래스가 객체로 생성될 때 무슨일이 일어나야 하는지
명시할 수 있게 해준다. 이는 다른 말로 객체 초기화라고도 불린다.(initialize)

파이썬은 생성자를 만드려면 init 함수라는 특별한 함수를 사용한다.
"""


class Car:
    def __init__(self):
        print("initialise attributes")


car_1 = Car()
car_2 = Car()

"""
여기서 self 키워드가 등장하는데, self는 실제 만들어지곡 있는,
또는 초기화 되고 있는 실제 객체를 뜻한다.
"""


class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    # 팔로우 기능
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
print(user_1.id)
print(user_1.user_name)
print(user_1.followers)

user_2 = User("002", "jack")
print(user_2.user_name)
print(user_2.id)

# 객체 생성시 생성자가 존재하는 클래스인데, arg에 넣지 않았다면 에러가 발생한다.
# ex) user3 = User()

"""
클래스와 객체를 다룰 때 self 키워드는 매우 중요해진다.
클래스 도면 내부에서 클래스로부터 만들어지는 객체를 지칭하는 방법이다.
즉 follow 메소드와 같은 생성된 자기 자신의 객체 내부 값을 바꿀 때 유용하게 사용된다.
"""
user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)
