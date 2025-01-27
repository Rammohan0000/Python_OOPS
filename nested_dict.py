car = {
    'hyundai': {
        'model': 'i10',
        'year': 2015,
        'price': 500000
    },
    'maruthi': {
        'model': 'swift',
        'year': 2016,
        'price': 600000
    },
    'tata': {
        'model': 'nano',
        'year': 2017,
        'price': 400000
    }
}
print(car.items())

def find_item_price(car,target_price):
    for item_id, item_details in car.items():
        if item_details['price'] == target_price:
            return item_id
    return None

target_price = 600000
result = find_item_price(car,target_price)
if result:
    print(f"Car with price {target_price} is {result}")   

#2nd Example for nested-dict
nested = {
    "ODI-Batsmen" : {
        'name':'Rohit',
        'total-runs': 30123,
        'best': 243
    },
    "Test-Batsmen" : {
        'name': 'Smith',
        'total-runs': 43567,
        'best': 218
    },
    "T-20-Batsmen": {
        'name': 'SKY',
        'total-runs':'3567',
        'best':123
    }
}
print(nested['Test-Batsmen']['name'])

def score(nested, target_runs):
    print(f"Players with total runs greater than {target_runs}:")
    for format_name, player_data in nested.items():
        if int(player_data['total-runs']) > target_runs:
            print(f"{player_data['name']} from {format_name} with {player_data['total-runs']} runs.")
score(nested, 40000)
