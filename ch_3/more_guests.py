people=['val','jobs','nixon']
people.insert(0,'mike')
people.insert(3,'angela')
people.append('dwight')
jobs_message=f"Hi {people[2].title()}! Come have dinner!"
val_message=f"Hi {people[1].title()}! Come have dinner!"
nixon_message=f"Hi {people[4].title()}! Come have dinner!"
mike_message=f"Hi {people[0].title()}! Come have dinner!"
angela_message=f"Hi {people[3].title()}! Come have dinner!"
dwight_message=f"Hi {people[5].title()}! Come have dinner!"
print(f"Hi {people[4].title()}, {people[1].title()}, and {people[2].title()}! We got a bigger table!")

print(dwight_message)
print(angela_message)
print(mike_message)
print(jobs_message)
print(nixon_message)
print(val_message)

print(f"Hey guys! There are {len(people)} people coming tonight!")

