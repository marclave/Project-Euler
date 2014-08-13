"""
Problem 15
https://projecteuler.net/problem=15
Highly divisible triangular number
"""
import math

def latticePath(d, r):
	
	return math.factorial(d + r) / (math.factorial(d)**2)

if __name__ == "__main__":

	print "================================="
	print "            Problem15            "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	print latticePath(20, 20)


	

	
