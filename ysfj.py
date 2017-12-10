import math

def ysfj(num):
	a = int(math.sqrt(num))+1
	for x in xrange(1,a):
		if num % x ==0:
			b = num/x
			print x
			print b

ysfj(98554799767)
