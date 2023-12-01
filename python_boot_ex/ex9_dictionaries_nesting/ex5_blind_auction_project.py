from ex5_blind_auction_art import logo
from replit import clear

# 프로그램 시작
con_game = True
auction_arr = []
rs_name = ""
rs_bid = 0
# 경매자 이름,금액 입력
print(logo)
print("Welcome to the secret auction program.")
while con_game:
    name = input("What is your name?: ")
    bid = input("What's your bid: $")
    auction_dict = {
        "name": name,
        "bid": bid,
    }
    auction_arr.append(auction_dict)
    con_game = False
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if bidders == 'yes':
        clear()
        con_game = True

for idx, item in enumerate(auction_arr):
    if idx == 0:
        rs_name = item['name']
        rs_bid = item['bid']
    else:
        if int(rs_bid) < int(item['bid']):
            rs_name = item['name']
            rs_bid = item['bid']

clear()
print(f"The winner is {rs_name} with a bid of ${rs_bid}")


"""
솔루션 정답은 딕셔너리 하나로 유추해낸다.
dict = {name:bid} 식으로
"""