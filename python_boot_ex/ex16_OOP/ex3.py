# 객체를 만들고 속성과 메소드에 접근하기

# 클래스 = 도면, 객체 = 도면을 실제 사용할 오브젝트
# ex
# car <- 객체, CarBlueprint <- 클래스
# car = CarBlueprint()

# 파이썬에서 클래스명 역시 파스칼 표기법으로 맨 처음 글자를 대문자로 시작한다.


from turtle import Turtle, Screen
import ex3_1

# print(ex3_1.another_variable)

# 객체 활용 예시
# timmy = turtle.Turtle()
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

# 객체의 속성 불러오기
my_scrren = Screen()
print(my_scrren.canvwidth)

# 객체의 메소드 불러오기
my_scrren.exitonclick()
