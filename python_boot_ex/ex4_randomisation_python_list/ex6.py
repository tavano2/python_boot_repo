# code Challenges
# 가로 A,B,C...
# 세로 1,2,3...

# 출제 전 변수 정리
line1 = ["□", "□", "□"]
line2 = ["□", "□", "□"]
line3 = ["□", "□", "□"]
resultMap = [line1, line2, line3]
# 문제 출제
print("Hiding your treasure! X marks the spot.")
position = input()
# 받은 변수로 보물맵 셋업
keyword = list(position)
x = int(keyword[1]) - 1
y = 0

if "B" == str(keyword[0]):
    y = 1
elif "C" == str(keyword[0]):
    y = 2

resultMap[x][y] = "★"

# 보물맵 결과 출력
print(f'{line1}\n{line2}\n{line3}')

# 솔루션 정답
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_idx = abc.index(letter)
num_idx = int(position[1]) - 1
resultMap[num_idx][letter_idx] = "★"
print(f'{line1}\n{line2}\n{line3}')