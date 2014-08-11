"""
Problem 4
https://projecteuler.net/problem=4
Largest two 3-digit palindrome product is 906609
"""

def getLargestPalindrome():

	largest = 0

	for a in range(1000, 0, -1):
		for b in range(1000, 0, -1):
			tempString = str(a*b)
			tempReversedString = tempString[::-1]
			tempLargest = int(tempString)
			if tempReversedString == tempString:
				if tempLargest > largest:
					largest = tempLargest

	print largest

				



if __name__ == "__main__":

	print "================================="
	print "            Problem4             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	getLargestPalindrome()
	
