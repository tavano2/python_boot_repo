print("Welcome to the tip calculator.")
""" 내가 쓴 정답
bill = input("What was the total bill? $")
percentage = input("What percentage top would you like to give? 10, 12 or 15? ")
rs_per = 0
if int(percentage) == 12:
    rs_per = 1.12
elif int(percentage) == 10:
    rs_per = 1.1
else:
    rs_per = 1.15
people = input("How many people to split the bill? ")
result = (float(bill) / int(people)) * rs_per
print(f"Each person should pay : ${round(result,2)}")
"""

# 솔루션 정답
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage top would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = round(bill_with_tip / people, 2)
# 마지막 부동 소수점을 0으로 처리하기 위한 포맷팅
result = "{:.2f}".format(bill_per_person)
print(f"Each person should pay : ${result}")
