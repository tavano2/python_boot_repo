# csv_arr = []
# with open("weather_data.csv", mode="r") as csv_file:
#     for line in csv_file:
#         csv_arr.append(line.strip())

# 파이썬에서는 csv 외부 모듈을 지원한다.

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 많은 양의 행과 열을 효과적으로 처리하고 싶을 때 판다스를 사용한다.

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)

print(data["temp"])
