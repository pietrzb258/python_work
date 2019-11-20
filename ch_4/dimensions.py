dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])


#code below throws TypeError. Cannot change the value of a tuple.
#dimensions[0]=250


for dimesion in dimensions:
    print(dimesion)


#how to write over a tuple
print("\nOriginal Dimesions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension
    )