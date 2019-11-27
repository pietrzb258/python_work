current_users = ['cactus49', 'python31', 'ADMIN', 'alien27', 'pizza_lover1312']
new_users = ['Cactus49', 'bpietrzyk', 'admin', 'visual_studio1', 'peachy22']
x = [z.lower() for z in current_users]
for y in new_users:
    if y.lower() in x:
        print(f"Sorry, the username {y.lower()} is already taken.")
    else:
        print(f"The username {y.lower()} is all yours!")
