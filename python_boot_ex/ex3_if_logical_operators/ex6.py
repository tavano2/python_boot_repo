# 여러 if 사용해 보기
print('Welcome to the Roller Coaster!')
height = int(input('What is your height in cm? '))
total_price = 0

if height >= 120:
    print('You can ride the Roller Coaster!')
    age = int(input("What is your age? "))
    if age < 12:
        print('Child tickets $5.')
        total_price += 5
    elif age <= 18:
        print('Youth tickets $7.')
        total_price += 7
    else:
        print('Adult tickets pay $12.')
        total_price += 12

    wants_photo = input("Do You want a phto taken? Y or N. ")

    if wants_photo == 'Y':
        total_price += 3

    print(f'Your final bill is {total_price}$')

else:
    print("You can't ride the Roller Coaster!")
