"""
Problem 6
https://projecteuler.net/problem=6
The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is:
	25164150
"""
def getSum():

	sumSquare = 0
	squareSum = 0

	for x in range(1,101):
		squareSum += x
		sumSquare += x**2
		
	print "Difference equeals " + str(squareSum**2 - sumSquare)
		

if __name__ == "__main__":

	print "================================="
	print "            Problem6             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	getSum()

	
	
