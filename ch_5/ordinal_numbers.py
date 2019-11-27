numbers = list(range(1,10))
for x in numbers:
    if x == 1:
        y = 'st'
    elif x == 2:
        y = 'nd'
    elif x == 3:
        y = 'rd'
    elif x > 3:
        y = 'th'
    print(f"{x}{y}.")
