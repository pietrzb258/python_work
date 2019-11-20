pizzas = ['pepperoni', 'cheese', 'hawaiian']
friends_pizzas = pizzas[:]
print(pizzas)
print(friends_pizzas)

pizzas.append('mushroom')
friends_pizzas.append('onion')

for pizza in pizzas:
    pizza
print(f"My favorite pizzas are {pizzas}!")

#for pizza in pizzas:
 #   print(f"I like {pizza.title()} pizza!\n")
#print("I really like pizza!")
