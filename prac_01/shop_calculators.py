total_price = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Number must more than 0")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items):
    price_of_items = float(input("Price of item: "))
    total_price += price_of_items
if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f}")