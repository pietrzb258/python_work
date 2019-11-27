usernames = ['cactus49','python31','ADMIN','alien27','pizza_lover1312']
for username in usernames:
    if username.lower() == 'admin':
        print(f"Welcome back {username}. Would you like a status report?")
    else:
        print(f"Welcome back {username}!")
