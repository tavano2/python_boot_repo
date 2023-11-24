# 가위바위 보 게임
# 0 가위 1 바위 2 보
import random

rock = '바위'
paper = '보'
scissors = '가위'

arr = [rock, paper, scissors]
my_num = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
com_num = random.randint(0, 2)
result = ''

if my_num > 2 or my_num < 0:
    print('Please Input Again')
else:
    print(f'Your chose : {arr[my_num]}')
    print(f'Computer Chose : {arr[com_num]}')

    if rock == arr[my_num]:
        if rock == arr[com_num]:
            result = 'Draw! Try Again'
        elif paper == arr[com_num]:
            result = 'You Lose..'
        else:
            result = 'You Win!'
    elif paper == arr[my_num]:
        if paper == arr[com_num]:
            result = 'Draw! Try Again'
        elif scissors == arr[com_num]:
            result = 'You Lose..'
        else:
            result = 'You Win!'
    else:
        if scissors == arr[com_num]:
            result = 'Draw! Try Again'
        elif rock == arr[com_num]:
            result = 'You Lose..'
        else:
            result = 'You Win!'
    print(result)

