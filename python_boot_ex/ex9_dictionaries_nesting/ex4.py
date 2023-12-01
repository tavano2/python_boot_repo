# code Challenges
country = input()
visits = int(input())
list_of_cities = eval(input())

travel_arr = [
    {"country": "France",
     "cities": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "cities": ["Paris", "Lille", "Dijon"],
     "total_visits": 5
     },
]


def add_new_country(c, v, lct):
    add_dict = {
        "country": c,
        "cities": lct,
        "total_visits": v
    }
    travel_arr.append(add_dict)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_arr[2]['country']} {travel_arr[2]['total_visits']} times.")
print(f"My favourite city was {travel_arr[2]['cities'][0]}")
