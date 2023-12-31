# 파이썬 패키지
# 지금까지는 각 모듈들을 import하여 공부했다.
# 패키지는 다른 사람이 쓴 코드 묶음이라는 점에서 모듈과 다르다.
# 어떤 목표나 목적을 달성하기 위해 아주 많은 파일이 모여 한 패키지가 되는 것이다.

# 예를 들어 표를 쉽게 작성하고 싶을 때 아스키코드가 아닌 특정 패키지를 찾아 사용하는 것이다.
# 파이썬 패키지들은 pypi.org에서 확인할 수 있다.


from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
