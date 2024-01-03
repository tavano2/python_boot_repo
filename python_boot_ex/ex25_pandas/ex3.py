import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data)
# color_data = data["Primary Fur Color"]
# print(color_data)
#
# cnt_gray = 0
# cnt_red = 0
# cnt_black = 0
#
# for item in color_data:
#     if item == "Gray":
#         cnt_gray += 1
#     elif item == "Cinnamon":
#         cnt_red += 1
#     elif item == "Black":
#         cnt_black += 1
#
# color_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [cnt_gray, cnt_red, cnt_black]
# }
#
# color_pd = pd.DataFrame(color_dict)
# color_pd.to_csv("squirrel_count.csv", index=False)

# 솔루션 정답

color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(data[data["Primary Fur Color"] == "Gray"]),
              len(data[data["Primary Fur Color"] == "Cinnamon"]),
              len(data[data["Primary Fur Color"] == "Black"])]
}

color_pd = pd.DataFrame(color_dict)
color_pd.to_csv("squirrel_count.csv", index=False)