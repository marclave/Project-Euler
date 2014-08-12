"""
Problem 7
https://projecteuler.net/problem=7

"""
def getPrime(n):
	sieve = [True] * (n+1)
	for p in range(2, n+1):
		if (sieve[p]):
			print p
			for i in range(p, n+1, p):
				sieve[i] = False

if __name__ == "__main__":

	print "================================="
	print "            Problem7             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	getPrime(6)


	
	
