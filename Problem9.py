"""
Problem 9
https://projecteuler.net/problem=9
Special Pythagorean triplet
"""

def getTriplet():
	for x in range(1,1001):
		for y in range(1,1001):
			temp = abs(-y - x)
			for z in range(1000,1, -temp):
				if x < y:
					if y < z:
						if x**2 + y**2 == z**2:
							if x + y + z == 1000:
								print x*y*z



if __name__ == "__main__":

	print "================================="
	print "            Problem9             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	getTriplet()

	
