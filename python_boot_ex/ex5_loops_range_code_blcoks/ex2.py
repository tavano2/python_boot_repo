# code Challenges
# sum이나 len 함수를 사용하지 않고 합계,평균 구하기
stuendt_heigths = input().split()
total = 0
stleng = 0
avg = 0
for n in range(0, len(stuendt_heigths)):
    stuendt_heigths[n] = int(stuendt_heigths[n])
    total += stuendt_heigths[n]
    stleng += 1
avg = total / stleng

print(f'total height = {total}')
print(f'number of students = {stleng}')
print(f'average height = {int(avg)}')
