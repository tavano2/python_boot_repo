# code Challenges
# fizzbuzz 게임 구현

num = 100

for idx in range(1, num + 1):
    if idx % 3 == 0 and idx % 5 == 0:
        print('FizzBuzz')
    elif idx % 3 == 0:
        print('Fizz')
    elif idx % 5 == 0:
        print('Buzz')
    else:
        print(idx)
