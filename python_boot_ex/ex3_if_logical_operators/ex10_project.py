print('Welcome to Treasure Island Your Mission is to find the Treasure')

chk_bool = False
ex1 = input('You\'re going "left" or "right"?: ')


if ex1.lower() == 'right':
    chk_bool = True
elif ex1.lower() == 'left':
    ex2 = input('Your swim or wait?: ')

    if not chk_bool and ex2.lower() == 'swim':
        chk_bool = True
    elif ex2.lower() == 'wait':
        ex3 = input('Your which Open the door? Red, Blue or Yellow?: ')
        if (not chk_bool and ex3.lower() == 'red') or (not chk_bool and ex3.lower() == 'blue'):
            chk_bool = True
        elif ex3.lower() != 'yellow':
            chk_bool = True
    else:
        chk_bool = True
else:
    chk_bool = True

if chk_bool:
    print('Game Over')
else:
    print('You Win!')

