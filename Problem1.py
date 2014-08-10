"""
Problem 1
https://projecteuler.net/problem=1
Sum of multiples of 3 and 5 below 1000 is 233168
"""

def multipleChecker():

	integer = 1
	sum = 0

	while integer < 1000:
		if (integer%3 == 0) or (integer%5 ==0):
			sum += integer
		integer	+= 1

	return sum



if __name__ == "__main__":

	print "================================="
	print "            Problem1             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	print(multipleChecker())

