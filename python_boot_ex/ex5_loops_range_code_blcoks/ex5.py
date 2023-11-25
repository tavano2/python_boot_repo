# code Challenges
# 1부터 특정 숫자 사이에 있는 모든 짝수의 합을 구하는 프로그램
target = int(input())

total = 0
for num in range(1, target + 1):
    if num % 2 == 0:
        total += num

print(total)

# 솔루션 정답1
even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)

# 솔루션 정답2
# 내가 쓴 것과 같음. step 활용 x -> % 연산자로 짝수 찾아 계산
