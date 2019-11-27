usernames = []
if usernames:
    for username in usernames:
        if username.lower() == 'admin':
            print(f"Welcome back {username}. Would you like a status report?")
        else:
            print(f"Welcome back {username}!")
else:
    print("No user selected.")
