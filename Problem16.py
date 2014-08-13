"""
Problem 16
https://projecteuler.net/problem=16
Power digit sum answer is 1366
"""

def powerSum(power):

	sum = 0
	result = str(2**power)

	for i in range(len(result)):
		sum += int(result[i])

	print sum




if __name__ == "__main__":

	print "================================="
	print "            Problem16            "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	powerSum(1000)


	

	
