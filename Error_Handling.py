# Error Handling 

# In this section, we're going to take a look at how we can handle and report 
# specific errors that come up when your Python program executes. Error handling 
# is a really important task that we need to perform inside of any code we write. 
# As humans, we're always going to write code that is prone to error, so let's 
# look at some basic error handling with a try_except statement in Python.

# Here we have what appears to be normal code that solves a simple equation
print("Let's solve the equation (x/2) / (x-y)")
x = float(input("Please enter a value for x: "))
y = float(input("Please enter a value for y: "))

z = (x/2) / (x-y)

print("Soving for (x/2) / (x-y) for values x = ", \
    x, "and y =", y, "we get the result:", z)

# And when I enter the following values I get an acurate result:

# Let's solve the equation (x/2) / (x-y)
# Please enter a value for x: 40
# Please enter a value for y: 20
Soving for (x/2) / (x-y) for values x =  40.0 and y = 20.0 we get the result: 1.0


# But what if a user where to enter a string value instead of a number value? We 
# would encounter an error like the one shown below:

# Let's solve the equation (x/2) / (x-y)
# Please enter a value for x: 40
# Please enter a value for y: twenty
Traceback (most recent call last):
  File "C:\Users\benjo\Documents\test.py", line 3, in <module>
    y = float(input("Please enter a value for y: "))
ValueError: could not convert string to float: 'twenty'


# What if they entered numbers that could "break" the equation? From the user's
# perspective, they did nothing wrong. But our program is frustrating because we 
# did not provide them with a clear explanation of why this happened. Note the 
# "ZeroDivisionError" for later.

# Let's solve the equation (x/2) / (x-y)
# Please enter a value for x: 40
# Please enter a value for y: 40
Traceback (most recent call last):
  File "C:\Users\benjo\Documents\test.py", line 5, in <module>
    z = (x/2) / (x-y)
ZeroDivisionError: float division by zero


# As developers, it is our responsibility to write good code that includes ways 
# of handling errors gracefully. So let's try to give this user a nice, clean 
# friendly message instead of an ugly, scary error message. Something that explains
# exactly what went wrong (if we know) and what the user can do, in order to 
# correct in the future. And then, maybe give them another chance to correct the 
# problem the problem we've found. 

# We can do this with something called a try block (which is pretty common in 
# procedural programming languages). You have your keyword, try and then your 
# block of code that you are checking for errors. Then you have your except statement
# (think of it as catching the error with a bucket). The "except" block of code 
# runs when an error occurs and handles them for you. You can have many buckets
# in your code to catch all kinds of errors if you like, and let's modify our code
# here to do that for us.

# Wrapping the code in a while loop, starting it off with a "try" and ending it
# with an "else" clause and a "finally" statement. 
while True:
	try:
		print("Let's solve the equation (x/2) / (x-y)")
		print("Please enter 0 to exit this program.")
		x = float(input("Please enter a value for x: "))
		y = float(input("Please enter a value for y: "))

		if x==0 or y==0:
			break

		z = (x/2) / (x-y)

# Catching the error here with an "exception", storing it in 
# variable "e" and printing it out in the "else" statement
	except Exception as e:
		print("There was an error with the code.")
		print("Error Message:", str(e))
	else:
		print("Soving for (x/2) / (x-y) for values x = ", \
    		x, "and y =", y, "we get the result:", z)
	finally:
		print("Clean up code goes here!")

# Let's solve the equation (x/2) / (x-y)
# Please enter a value for x: 40
# Please enter a value for y: 40
There was an error with the code.
Error Message: float division by zero


# This is a good start, but let's dive a little deeper. Python actually has some 
# "exception" functions we can use in our code and you can learn more about them 
# in the documentation: https://docs.python.org/2/library/exceptions.html

# Let's use Python's "ZeroDivisionError exception" function to make our code a 
# little cleaner and see it in action.
while True:
	try:
		print("Let's solve the equation (x/2) / (x-y)")
		print("Please enter 0 to exit this program.")
		x = float(input("Please enter a value for x: "))
		y = float(input("Please enter a value for y: "))

		if x==0 or y==0:
			break

		z = (x/2) / (x-y)

	except ZeroDivisionError as e:
		print("There was an error with the code.")
		print("You keyed in a value that caused a division by zero :(")
	else:
		print("Soving for (x/2) / (x-y) for values x = ", \
    		x, "and y =", y, "we get the result:", z)
	finally:
		print("Clean up code goes here!")

# Please enter a value for x: 40
# Please enter a value for y: 40
There was an error with the code.
You keyed in a value that caused a division by zero :(


# Now I want to finish up this program by adding multiple exceptions to my program. 
# I have my ZeroDivisionError, ValueError and a sort of "catch all" exception 
# bucket now in my program. Give it a try!
while True:
	try:
		print("Let's solve the equation (x/2) / (x-y)")
		print("Please enter 0 to exit this program.")
		x = float(input("Please enter a value for x: "))
		y = float(input("Please enter a value for y: "))

		if x==0 or y==0:
			break

		z = (x/2) / (x-y)

	except ZeroDivisionError as e:
		print("There was an error with the code.")
		print("You keyed in a value that caused a division by zero.")
	except ValueError as e:
		print("There was an error with the code.")
		print("You keyed in a text value when a number was expected.")
	except Exception as e:
		print("There was an unknown error with the code.")
		print("Error Message:", str(e))
	else:
		print("Soving for (x/2) / (x-y) for values x = ", \
    		x, "and y =", y, "we get the result:", z)
	finally:
		print("Clean up code goes here!")
