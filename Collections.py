# Collections

# Collections allow you to have multiple different values stored in a single variable 
# so that you can work with them collectively. We're going to look at examples of 
# a couple of collection types; lists and dictionaries.  
#
# In Python, lists are simply a list of values stored in memory alongside an index 
# and easy to define. You define your variable names with an equal sign (your 
# assignment operator) and then the values.
#
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#
# A dictionary is a key-value pair. We're going to have a key and a value, only 
# the key doesn't have to be a sequential list of numbers that are assigned by 
# the computer. The key is anything that you want it to be, defined by us as 
# programmers.
#
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# Here is a simple list of numbers.
x = [1, 2, 3, 4, 5]

print(x)

# Output:
# [1, 2, 3, 4, 5]

# Now I want to specify which index of the list I want to print out.
x = [1, 2, 3, 4, 5]

print(x[2])

# Output
# 3

# We can use the "length" function to see how many items are in a list.
numbers = [1, 2, 3, 4, 5]

x = len(numbers)
print(x)

# Output:
# 5

# We can list out tuples here...
x = (1, 2, 3, 4, 5)

print(x)

# Output
# (1, 2, 3, 4, 5)

# And make a dictionary like so...
x = {'Alice': 1, 'Bob': 2, 'Cathy': 3}

print(x)
print(x['Bob'])

# Output:
# {'Alice': 1, 'Bob': 2, 'Cathy': 3}
# 2

# Here is another way we could call out a specific item. 
names = ['Alice', 'Bob', 'Cathy', 'Doug', 'Elise']

x = names.index('Bob')
print(x)

for index in range(0, len(names)):
	print(names[index], 'is found at index', index)

# Output
# 1
# Alice is found at index 0
# Bob is found at index 1
# Cathy is found at index 2
# Doug is found at index 3
# Elise is found at index 4


# Here are a few functions that would allow use to makes changes to lists. 
names = ['Alice', 'Bob', 'Cathy', 'Doug', 'Elise', 'Frank']
print(names)

raw_NewIndex = input('Please enter the index to replace: ')
NewIndex = int(raw_NewIndex)

newName = input('Please enter the name to put in the index: ')

names[NewIndex] = newName
print(names)

newName = input('Please enter the name to add to the list: ')
names.append(newName)
print(names)

remName = input('Please enter the name you wish to remove from the list: ')
names.remove(remName)
print(names)


# Here is a dictionary with a name-age (key-value) pair and I want to print out 
# the age of everyone using the function below.
ages = {'Alice': 21, 'Bob': 24, 'Cathy': 30, 'Doug': 19}
print(ages)

for age in ages:
	print('The age of', age, 'is', ages[age])

# Output:
# {'Alice': 21, 'Bob': 24, 'Cathy': 30, 'Doug': 19}
# The age of Alice is 21
# The age of Bob is 24
# The age of Cathy is 30
# The age of Doug is 19


# Now just like we did with the list above, let's use some functions to add or
# remove keys and values. 
ages = {'Alice': 21, 'Bob': 24, 'Cathy': 30, 'Doug': 19}
print(ages)

newKey = input('Please enter the key you wish to change: ')
newVal = input('Please enter the value of the new key: ')

ages[newKey] = newVal
print(ages)

newKey = input('Please enter a new key you wish to add: ')
newVal = input('Please enter the value of the new key: ')

ages[newKey] = newVal
print(ages)

remKey = input('Enter a key you wish to remove: ')

del ages[remKey]
print(ages)