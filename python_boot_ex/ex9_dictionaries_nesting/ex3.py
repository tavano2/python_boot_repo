# 중첩
"""
파이선 자료구조는 중첩구조를 가질 수 있다.
{
    key: [List],
    key2: {dict},
}
중첩 자료구조를 사용할 경우 조금 더 복잡하고 어려워지지만
데이터를 저장하는데 있어서 더 다양한 선택지를 제공해준다.
"""

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# 딕셔너리안에 리스트 중첩
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# 리스트안에 리스트 중첩 <- 유용한 자료구조가 아니여서 자주 쓰이지 않음
tt_arr = ["A", "B", "C", ["D", "E"]]

# 딕셔너리 안 딕셔너리 중첩
travel_log = {
    "France": {
                "cities_visited": ["Paris", "Lille", "Dijon"],
                "total_visits": 12
               },
    "Germany": {
                "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
                "food": ["Beer", "Fork"],
                "football": ["Dor", "Bayn"]
                }
}

# 리스트안에 딕셔너리 중첩
travel_arr = [{"coutry": "France",
               "cities_visited": ["Paris", "Lille", "Dijon"],
               "total_visits": 12
               },
              {"coutry": "Germany",
               "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
               "food": ["Beer", "Fork"],
               "football": ["Dor", "Bayn"]
               }
              ]

