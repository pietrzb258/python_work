age = 21
if age <= 4:
    print("Your admission cost is Free!")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 70
if age <= 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40
print(f"\nYour admission price is ${price}.")

age = 22
if age <= 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"\nYour admission price is ${price}.")
