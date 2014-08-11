"""
Problem 3
https://projecteuler.net/problem=3
Largest prime factor answer is 6857
"""

def largestFactor(limit):

	i = 2 # Start at 2 to avoid infinite loop

	while i**2 < limit:
		while limit%i == 0:
			limit = limit/i
		i += 1

	print limit

if __name__ == "__main__":

	print "================================="
	print "            Problem3             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""
	
	largestFactor(600851475143)
