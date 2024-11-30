#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rim",
}

#Nesting a List in a Dictionary
# Nesting dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["Germany"])


# Nesting Dictionary in a List

travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    },
]
starting_dictionary = {
    "a":9,
    "b":8,
}

final_dictionary = {
    "a":9,
    "b":8,
    "c":7
}

starting_dictionary["c"] = 7
print(starting_dictionary)
#print(starting_dictionary[1])

for key in starting_dictionary:
    print(starting_dictionary[key])


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])




