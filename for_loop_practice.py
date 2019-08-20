# for loop practice

# list of words
a = ["apple", "banana", "carrot", "cranberries", "raisins", "walnuts"]

for i in a:
	print(i)



# list of numbers

b = [1, 3, 6, 9, 11, 13]

total = 0

for i in b:
	total = total + b

print(total)



# using the range function for cleaner code with big data set
# using the list function to see what is inside the range

# list of numbers ranging from 1 to 1000
c = list(range(1, 1001))

print(c)



# create a for loop that adds all the numbers together
total_one = 0

for i in range(1, 1001):
   #total_num = total_num + i
	total_one += i

print(total_one)



# for loop that looks for numbers that are multiples
# of three in a range   
total_two = 0

for i in range (1, 14) :
	if i % 3 == 0:
		total_two += i

print(total_two)



# for loop that adds all the multiples of 3 and 9 in a range
total_three = 0 

for i in range(1, 100):
	if(i % 3 and i % 9) == 0:
		total_three += i

print(total_three) 
