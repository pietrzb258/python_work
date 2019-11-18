people=['einstein','jobs','nixon']
jobs_message=f"Hi {people[1].title()}! Come have dinner!"
einstein_message=f"Hi {people[0].title()}! Come have dinner!"
nixon_message=f"Hi {people[2].title()}! Come have dinner!"
print(jobs_message)
print(nixon_message)
print(einstein_message)

print(people[0].title())
people.remove('einstein')
people.insert(0, 'val')
val_message=f"Hi {people[0].title()}! Come have dinner!"
print(jobs_message)
print(nixon_message)
print(val_message)
