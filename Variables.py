# Variables 

# Variables allow you to assign and store value for a given piece of information. They are implicitly declared and strong-typed. Here some
# of the basic strong-typed variables you can store in your program. 

# Numeric
# String
# List 
# Tuple
# Dictionary

# The pieces of code in "/Variables" will be executed each line top to bottom, and assign the value on the left side of equal sign
# (assignment operator) to the variable on the right side of the operator.

UserName = 'benjohn13'
FullName = 'Ben Belcher'

print(UserName)
print(FullName)

AltName = UserName
IncorrectName = 'FullName'

print(AltName)
print (IncorrectName)

# Output

# benjohn13
# Ben Belcher
# benjohn13
# FullName


# Here is some example code using some of the different basic data types.

# I used double quotes here for the String variable, which
# will allow me to use single quotes inside the string 
varString = "This is a string variable. It can have" \
            "any combination of letters, numbers or" \
            "special characters."

# You can use this variable for normal integers ranges
varInteger = 11

# For really long integers, you can add the letter "L" at 
# the end to specify this will be a long integer.
varLong = 12345L

# Using float here for decimal places
varFloat = 1300.11

varList = [1, 2, 3.5, "Ben", "Sarah", "James"]

varTuple = (1, 2, 3.1, "Alice", "Bob", "Cathy")

varDictionary = { 'First': 'This is the first item in the dictionary',
                 'Second': 'This is the second item in the dictionary' }

print(varString)
print(varInteger)
print(varLong)
print(varFloat)
print(varList)
print(varTuple)
print(varDictionary)

# Output

# This is a string variable. It can have 
# any combination of letters, numbers or 
# special characters.
# 11
# 12345
# 1300.11
# [1, 2, 3.5, 'Ben', 'Sarah', 'James']
# (1, 2, 3.1, 'Alice', 'Bob', 'Cathy')
# { 'Second': 'This is the second item in the dictionary', 
# 'First': 'This is the first item in the dictionary'}
