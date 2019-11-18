states=['new york','utah','alabama','georgia','mississippi','virginia']
print(sorted(states))
print(states)
states.sort()
print(states)
states.sort(reverse=True)
print(states)
alabama=states.pop(5)
georgia=states.pop(4)
print(states)
print(georgia)
print(len(states))
dream='new york'
states.remove(dream)
print(f"My dream place to visit is {dream.title()}!")
print(states)
print(len(states))
del states[2]
print(states)
states.append('vermont')
print(states)
message=f"My favorite state tp visit is {states[2].title()}!"
print(message)
print(states[-1].title())
