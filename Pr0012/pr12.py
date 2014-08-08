`## Goal: First triangle number with 500 divisors

## Method: The nth triangle number is represented as n*(n+1)/2
#	We can take advantage of consecutive integers being coprime
#	So, n and n+1 are coprime. Therefore, if n is even, n/2 and n+1 are coprime
#		(since we're just removing the 2 divisor of n, which n+1 doesn't have)
#	If n+1 is even, the same applies
#	Since they're coprime, the number of divisors for the nth triangle number
#		must be equal to the number of divisors for n/2 and n+1 (or n+1/2 and n)

n = 0
five_hundred_divisor_number = 0
while not five_hundred_divisor_number:
	n += 1
	coprime1 = n
	coprime2 = n+1
	if n % 2 == 0:
		coprime1 /= 2
	else:
		coprime2 /= 2
	#end if n even
	
	#num_divisors = divisors(coprime1) + divisors(coprime2)