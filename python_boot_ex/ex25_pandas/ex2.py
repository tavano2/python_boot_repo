import pandas as pd

data = pd.read_csv("weather_data.csv")
# 데이터 프레임
# print(type(data))
# 시리즈
# print(type(data["temp"]))

"""
판다스의 두 가지 주요 데이터 구조인 series 와 data frame에 대해 알아보자

data frame : 데이터 프레임은 전체 표와 같은 것이라 이해하자
엑셀 파일이나 구글 스프레이트 시트 역시 데이터 프레임으로 인식한다.

series : 열에 관한 1차원 데이터 배열을 일컫는다.
"""

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average = data["temp"].mean()
# print(average)
#
# temp_max = data["temp"].max()
# print(temp_max)
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
print(monday.condition)
print((monday.temp[0] * 9/5) + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

stu_data = pd.DataFrame(data_dict)
stu_data.to_csv("new_data.csv", index=False)


