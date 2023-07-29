
# List goes in brackets '[]'
family = ['Phillip', 'TJ', 'Valerie', 'Mom', 'Dad']

print(family)
print(type(family))

#Subsetting list


#To subset the first index, use list_name[0], 0 represents the first 

print(family[0])

#subsetting the last index
print(family[-1])

#list slicing [start : end]

print(family[1:5])


# Manipulating Lists

family.append('chance')

print(family)


#functions and packages

ages = [32,33,54,36,68]

print(min(ages))

help(min)