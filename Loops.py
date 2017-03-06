# Loops

# Computers make quick, efficient, and accurate calculation machines that can perform
# repetitive tasks over and over and over. They're great at performing math calculations
# where a human might take a long time and be prone to make errors. Once a computer has
# been taught something, it can perform that calculation very quickly. 
#
# The key comes in providing the computer with appropriate instructions. Loops are a good 
# way to provide instructutions for these kind of tasks and allow us to simplify those 
# instructions. Rather than having to write out hundreds of line of code with multiple "if"
# statements, we can create a few lines of logic that utilize a few built in functions.
#
# There are many ways we could write out "for loops" and "while loops". But it's always
# best practice to try to make your code as simple, readable and powerful as agile as 
# possible. Below are just a few examples of ways we could use loops in our programs.    


# Here we have a simple list of names and a "for loop" for them.

names = ['Alice', 'Bob', 'Cathy', 'Doug']

print (names)

for name in names:
	print(name, 'is  great person.')

# Output
# ['Alice', 'Bob', 'Cathy', 'Doug']
# Alice is  great person.
# Bob is  great person.
# Cathy is  great person.
# Doug is  great person.


# We could also do this with numbers using the same list and loop.

numbers = [1, 2, 3, 4]

print (numbers)

for number in numbers:
	print(number)

# Output
# [1, 2, 3, 4]
# 1
# 2
# 3
# 4


# Now I'll simplify this "for loop" with the range function (see docs below to learn more).
# https://docs.python.org/2/library/functions.html#range

numbers = range(1, 5)

print (numbers)

for number in numbers:
	print(number)

# Output:
# [1, 2, 3, 4]
# 1
# 2
# 3
# 4


# Here is a "for loop" test for numbers to see if the number is a prime number between 2 and 10.

num = 3
prime = True #Heads up, Python is case sensitive here for True and False

for test in range(2, 10):
	if num % test == 0 and num != test:
		print(num, 'equals', test, '*', num/test)
		prime = False

if prime: 
	print(num, 'is a prime number!')
else:
	print(num, 'is not a prime number.')

# Output:
# 3 is a prime number!


# Here I want test against a larger number and use the break command to prevent the code from
# running five thousand times (if it's not a prime number) and simplify the loop even more. 
# https://docs.python.org/2/reference/simple_stmts.html#break

num = 5011

for test in range(2, num):
	if num % test == 0 and num != test:
		print(num, 'equals', test, '*', num/test)
		print(num, 'is not a prime number.')
		break

else: 
	print(num, 'is a prime number!')

# Output
# 5011 is a prime number!


# Now let's take a look at a "while loop".

sum = 0
add = 1

while add != 0:
	print('The current sum is:', sum)
	print('How much would you like add now?', end = '')
	raw_add = input(raw_add)
	sum = sum + add

# Output
# The current sum is: 0
# How much would you like add now?(Type 0 to end the program): 1
# The current sum is: 1
# How much would you like add now?(Type 0 to end the program): 2
# The current sum is: 3
# How much would you like add now?(Type 0 to end the program): 3
# The current sum is: 6
# How much would you like add now?(Type 0 to end the program): 0
# >>> 