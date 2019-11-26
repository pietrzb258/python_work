motorcycle='ducati'
print(motorcycle=='ducati')
print(motorcycle=='yamaha')
print("\n")

name='Brandon'
print(name=='brandon')
print(name.lower()=='brandon')
print("\n")

age_0=21
print(age_0==21)
print(age_0==20)
print("\n")

age_1=21
print(age_1>20)
print(age_1>40)
print("\n")

age_2=21
print(age_2<40)
print(age_2<18)
print("\n")

age_3=21
print(age_3>=50)
print(age_3>=18)
print("\n")

age_4=21
print(age_4<= 21)
print(age_4<=18)
print("\n")

cell_phone='samsung'
print(cell_phone == 'apple' or cell_phone == 'samsung')
print(cell_phone=='apple' or cell_phone=='motorola')
print("\n")

tablet='iPad'
number=1
print(tablet.lower()=='ipad' and number!=2)
print(tablet.lower()=='android' and number==0)
print("\n")

fruits=['apple','banana','grapes','peach']
good_fruit='banana'
if good_fruit in fruits:
    print("Bananas!!")
else:
    print("No Bananas!")
fruits.pop(1)
if good_fruit in fruits:
    print("\nBananas!!")
else:
    print("\nNo Bananas!")

print("\nAre bananas in the list? I think no.")
print('banana' in fruits)

print("\nAre anchovies in the list? I think no!")
print('anchovies' not in fruits)
fruits.append('anchovies')
print('anchovies' not in fruits)

