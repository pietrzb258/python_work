age = 19
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age > 64:
    stage = 'elder'
print(f"The stage in life you are in is {stage.title()}!")
