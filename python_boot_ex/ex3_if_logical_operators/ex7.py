# 자동 피자 주문 프로그램
# code Challenges

"""
size
small : $15
medium : $20
large : $25

pepperoni
small : $2
medium, large : $3

extra chease : $1
"""


print('Thank you for choosing Python Pizza Deliveries')
size = input("What size pizza Do You Want? S, M, or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_chease = input('Do you want extra chease? Y or N. ')
total_price = 0
chk_pepperoni = False
chk_chease = False

if add_pepperoni == 'Y':
    chk_pepperoni = True

if extra_chease == 'Y':
    chk_chease = True

if size == 'S':
    total_price += 15
    if chk_pepperoni:
        total_price += 2
elif size == 'M':
    total_price += 20
    if chk_pepperoni:
        total_price += 3
else:
    total_price += 25
    if chk_pepperoni:
        total_price += 3

if chk_chease:
    total_price += 1

print(f'Thank You for choosing Python Pizza Deliveries: Your final bill is: ${total_price}')

# 솔루션 정답 코드는 거의 비슷하고, 페퍼로니 체크 부분만 조건문이 따로 생성되었다.
