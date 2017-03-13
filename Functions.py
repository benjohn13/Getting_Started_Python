# Functions

# Functions are a logical construct that a lot of programming languages offer.
# They basically allow you to write a piece of code, set it aside, and then execute 
# it on demand as many times as you like throughout the lifetime of your program.
# We're going to take a look at how we can call functions, excute functions, define
# functions and how we can import functions from external files. 

# Here we see the basic "print()" function. I create the variables a, b and C and
# pass it in the print() function. Now the computer doesn't know how to how to print 
# a statement to the screen. The instructions that the computer actually needs to 
# execute the print() function are at a lower level and is much more complex. But 
# because that's such a common task, the people who made Python took all the code 
# that causes that information to appear inside of your screen and they bundled 
# it up. Now all you have to do is tell the program to print() and it will do
# it for you every time!
a = 10 
b = 15

c = a * b

print(c)

# Output
# 150   


# Here is an example of the "input()" function, which allows the user of my program
# to enter a variable and makes the outcome more dynamic.
a = input("Hello, what is your name?: ")

print("Thanks,", a)

# Output
# Thanks, {Any text string entered}


# Now I could ask for a number and explicitly call out the input() to be an integer.
a = int(input("Hi, Please enter a number you would like mupltiplied by 10: "))
b = a * 10

print(a, "mupltiplied by 10 equals", b)


# Here we're going to create our own function. We'll use "def" to define it/ give
# it a name, and then we'll indent the code below that performs the finction. 
def exponent(a,b):
	c = a ** b
	print(c)

base = int(input("Hi! Please enter the base value: "))
exponentValue = int(input("Now enter your exponent value: "))

exponent(base,exponentValue)


# Now a really cool thing you can do with Python is create a separate file, store
# a bunch of functions that you make and that becomes a library you can call on!
# For example, let's say I create a file, call it ben.py and store the function 
# above in there with others. Then I could import that library in a sperate view
# and use the function like so:
import ben

base = int(input("Hi! Please enter the base value: "))
exponentValue = int(input("Now enter your exponent value: "))

# Calling the "ben.py" library and specifying which function I want to use:
ben.exponent(base,exponentValue)