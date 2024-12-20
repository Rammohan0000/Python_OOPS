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