# code Challenges
# input에 넣은 점수중 제일 높은 값 찾기
std_scores = input().split()

max_value = 0
for item in range(0, len(std_scores)):
    if max_value < int(std_scores[item]):
        max_value = int(std_scores[item])

print(f'The Highest score in the class in : {max_value}')
