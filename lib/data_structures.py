spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5] 

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = "🌶"  * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods: 
        if food["cuisine"] == cuisine:
            return food 

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat = "🌶"  * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    # takes a list of spicy_foods
    # returns an integer
    # representing the average heat level of all the spicy foods in the array
    total_heat = 0
    for food in spicy_foods:
        total_heat  = total_heat + food["heat_level"]
    number_of_items = len(spicy_foods)
    average = total_heat / number_of_items
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    # define a function
    # that takes a list of spicy_foods
    # and a new spicy_food
    # returns the original list with new spicy_food added
    spicy_foods.append(spicy_food)
    return spicy_foods
