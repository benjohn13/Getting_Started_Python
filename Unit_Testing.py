# Unit Testing

# As developers, we're expected to deliver the functional, tested code at every 
# step along the process. That means testing your code as you write it, which is 
# really impoirtant. There's a lot of different levels and a lot of different layers 
# to testing. 

# There is system testing, which takes a look at the overall system and ensures 
# that it's working the way that it's expected to. There is user acceptance testing, 
# which focuses on the user and makes sure that their experience is what they believe 
# it should be. We're going to look at unit testing, which is involved at the lowest 
# level; taking the individual units themselves and running checks against them 
# to make sure the units work exactly the way that they are supposed to at the 
# smallest, most discrete level.

# This means writing unit testing scripts. Testing scripts can be intimidating
# at first, but they're not all that complicated. The basic underlying piece of 
# a unit testing script is what we call the "assertion" and the assertion is a 
# statement that we expect to evaluate in a certain way. So let's go ahead and get
# started by writing some basic unit testing scripts and here is the documentation
# for unit testing in Python 3.6.

# https://docs.python.org/3/library/unittest.html


# Here we have a basic exponent function calculating five to the third power
def ExponentCalc(x, y):
	return x ** y

print(ExponentCalc(5, 3))


# The result will be 125, but I want to write a script that will ensure the result 
# fits the parameters I consider to be success. So let's import the "unittest" library:
import unittest

def ExponentCalc(x, y):
	return x ** y

# Making a class with functions to test this assertion
class ExponentCalcTest(unittest.TestCase):
	def testSuccess(self):
		result = ExponentCalc(5, 3)
		self.assertEqual(result, 125)

	def testFailure(self):
		result = ExponentCalc(5, 3)
		self.assertNotEqual(result, 124)

unittest.main()

# Output:
..
----------------------------------------------------------------------
Ran 2 tests in 0.006s

OK


# The program ran two tests and they came back "Ok", so that's great! But I'll 
# change the result number for the first assertion to show a failure:
import unittest

def ExponentCalc(x, y):
	return x ** y

# Making a class with functions to test this assertion
class ExponentCalcTest(unittest.TestCase):
	def testSuccess(self):
		result = ExponentCalc(5, 3)
		self.assertEqual(result, 10)

	def testFailure(self):
		result = ExponentCalc(5, 3)
		self.assertNotEqual(result, 124)

unittest.main()

# Output:
.F
======================================================================
FAIL: testSuccess (__main__.ExponentCalcTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\benjo\Documents\test.py", line 10, in testSuccess
    self.assertEqual(result, 10)
AssertionError: 125 != 10

----------------------------------------------------------------------
Ran 2 tests in 0.010s

FAILED (failures=1)


# And there you have it. Unit Testing at a very basic level. It may be something
# you're really into. But from personal experience, I have found unit testing to
# be an essential part of development work and can really challenge you to imporve
# code. If you want to learn more, check out the Python docs above and enjoy! 