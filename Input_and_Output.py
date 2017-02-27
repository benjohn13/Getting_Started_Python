# Input and Output

# Here we have the "print" function with a single parameter; the text value, 'Hello World!'
# You can learn more at: https://docs.python.org/2/library/functions.html#print

print('Hello World!')

# When looking at the "print" function documentation, it has a couple of cool named-parameters
# that can be added. For example in Python 3.x,

print('Hello', 'World', '!', sep='')

# Output:
# HelloWorld!

# I gave the sep='' parameter a non-space string argument, which smooshed the values together 
# with no spaces. Another named-parameter, 

print('Hello', 'World', '!', end='')

print('Hello', 'World', '!', sep='')

# Output:
# HelloWorld!HelloWorld!

# Normally there is a line break when a new print statement begins, but in this case
# I explicitely told the program to have no spaces or new line breaks with the non-
# space string argument in the end'' named parameter.

# Now I want to call the "compare" function to compare multiple values
# and will separate the values with commas to establish parameters.

cmp(11, 13)

# Output:
# -1

# Some functions can only accept one value, others might take two, or as many as you want.
# To look at some other functions, or to understand them better, check out the Python 
# documentation here: https://docs.python.org/2/library/functions.html#cmp

# Now let's create a program that will allow us to get varying input from our users 
# instead instead of just playing with static code. And since I am using Python 3.6 
# in this example, I will be using the 'input' function instead of 'raw_input' which 
# is needed for Python 2.x versions.

userName = input('Please enter your name: ')
age = input('Please enter your age: ') 

factor = 2 
finalAge = age + factor
multAge = age * factor
divAge = age / factor

print('In', factor, 'years you will be', finalAge, 'years old', userName)
print('Your age multiplied by', factor, 'is', multAge)
print('Your age divided by', factor, 'is', divAge)

# Output: 
# Please enter your name: Ben 
# Please enter your age: 20
# In 2 years you will be 22 years old Ben
# Your age multiplied by 2 is 40
# Your age divided by 2 is 10

# Now since I am letting the user input their age in a raw format, they could enter
# an odd number and Python will round down when it divides the number. A user could 
# also write in a number with text rather than entering a number, which will cause an 
# error. This is where we will want to code in error handling, maybe make it so the user
# always has to enter a number and/or have the program handle it like a float so it 
# divide number into a decimal. 

divAge = float(age) / factor