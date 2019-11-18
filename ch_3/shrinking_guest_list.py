people=['mike','val','jobs','angela','nixon','dwight']
print("Hi Guys, I can only invite two people!")
print(people)
dwight=people.pop(5)
print(f"Sorry {dwight.title()}!")
nixon=people.pop(4)
print(f"Sorry {nixon.title()}!")
angela=people.pop(3)
print(f"Sorry {angela.title()}!")
jobs=people.pop(2)
print(f"Sorry {jobs.title()}!")
print(f"Hi {people[0].title()} and {people[1].title()}, you're still invited!")
del people[1]
del people[0]
print(people)
