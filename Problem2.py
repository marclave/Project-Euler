"""
Problem 2
https://projecteuler.net/problem=2
Even Fibonacci numbers answer is 4613732
"""

EVEN_SUM = 2 # Starts at two because 2 is even
def fibonacci(a,b):
	global EVEN_SUM
	if a <= 4000000 and b<= 4000000:
		c = b + a
		if c%2 == 0:
			EVEN_SUM += c
		fibonacci(b,c)
	else:
		return

if __name__ == "__main__":

	print "================================="
	print "            Problem2             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	fibonacci(1,2)
	print EVEN_SUM

