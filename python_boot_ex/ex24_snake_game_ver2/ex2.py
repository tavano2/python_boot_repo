"""
파일의 읽고 쓰기 방법 학습하기

"""

# 1. open 내장 함수 사용하기
file = open("my_file.txt")
contents = file.read()
print(contents)
# I/O는 자원을 사용하기 때문에 종료시 자원을 닫아야 한다.
file.close()

# 2. with 키워드 사용
with open("new_file.txt", mode="a") as file:
    file.write("New Text.")
