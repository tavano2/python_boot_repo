"""
파일의 경로에 대해

절대 경로 : root를 기준으로 파일이나 폴더 경로를 찾는 방법 (/ = root)
상대 경로 : 작업 디렉토리 기준으로 파일이나 폴더 경로를 찾는 방법 (./ = 현재 작업 폴더 ../ = 상위 폴더)
상대 경로일 경우 ./를 생략해서 사용 가능하다.
"""
# C:\Users\Tavano\Desktop
with open("/Users/Tavano/Desktop/my_file.txt", mode="r") as file:
    for line in file:
        print(line)

print("\n")

# 상대경로 학습
with open("../../../../Desktop/my_file.txt", mode="r") as file:
    for line in file:
        print(line)
