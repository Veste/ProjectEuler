## Goal: Sum the primes below 2000000

## Method: Sieve of Eratosthenes
# Tag the prime numbers below 2000000

top = 2000001
sieve = [False]*top
sum = 0

for i in range(2, top):
	if sieve[i] == False:
		sum += i
		p = i*2
		for j in range(p, top, i):
			sieve[j] = True
		#end for
	#end if
#end for

print("Sum: ", sum)