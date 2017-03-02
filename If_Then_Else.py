# If... Then... Else

# If-Then-Else statements are conditional statements inside of Python. Almost every 
# language has some variation of this and it's an important logical clause inside 
# of programming. They allows you to set up multiple blocks of code that may or may 
# not be executed depending on the state of your program, or the context that it's 
# running in, the value of a variable. So it's a really important logical structure 
# inside of any programming language and I'm going to demonstrate an example here.

name = input('Hi! What is your name?: ')
age = int(input('How old are you?: '))

if age >= 21:
	print('Thank you', name,'!', 'You are old enough to party here!')
elif age >= 18:
	print('Thanks', name,'! You are allowed to come in, but you are not old enough to drink.')
else:
	print('Sorry', name, 'but you are not old enough to party in this club.')