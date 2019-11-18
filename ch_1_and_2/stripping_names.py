# Brandon Pietrzyk 11/16/2019. This program show how to remove whitespaces surrounding output. 
first_name = "Brandon"
last_name = "Pietrzyk"
full_name = f"\t{first_name} {last_name}\n"
print(full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())

