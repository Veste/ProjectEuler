## Goal: First triangle number with 500 divisors

## Method: The nth triangle number is represented as n*(n+1)/2
#	We can take advantage of consecutive integers being coprime
#   https://proofwiki.org/wiki/Consecutive_Integers_are_Coprime
#	So, n and n+1 are coprime. Therefore, if n is even, n/2 and n+1 are coprime
#		(since we're just removing the 2 divisor of n, which n+1 doesn't have)
#	If n+1 is even, the same applies
#	Since they're coprime, the number of divisors for the nth triangle number
#		must be equal to the number of divisors for n/2 and n+1 (or n+1/2 and n)

import math

def prime_fact( num ):
  prime_fact_list = []
  test = 2
  test_count = 0

  while num > 1:
    if num % test == 0:
      test_count += 1
      num /= test
    else:
      if test_count >= 1:
        prime_fact_list.append( (test, test_count) )
      test += 1
      test_count = 0
    #end if
  #end while
  if test_count >= 1:
    prime_fact_list.append( (test, test_count) )

  return prime_fact_list

n = 0
five_hundred_divisor_number = 0
while not five_hundred_divisor_number:
  n += 1
  num = (n * (n+1))/2

  coprime1 = n
  coprime2 = n+1
  if n % 2 == 0:
    coprime1 /= 2
  else:
    coprime2 /= 2
  #end if n even or odd
  coprime1_pfact = prime_fact(coprime1)
  coprime2_pfact = prime_fact(coprime2)

  div_product = 1

  c1_tup = None
  if coprime1_pfact:
    c1_tup = coprime1_pfact.pop(0)

  c2_tup = None
  if coprime2_pfact:
    c2_tup = coprime2_pfact.pop(0)

  if coprime1_pfact and coprime2_pfact:
    # While both lists aren't empty...
    while not c1_tup is None and not c2_tup is None:
      if c1_tup[0] > c2_tup[0]:
        div_product = div_product * (c2_tup[1] + 1)
        if coprime2_pfact:
          c2_tup = coprime2_pfact.pop(0)
        else:
          c2_tup = None
      elif c1_tup[0] < c2_tup[0]:
        div_product = div_product * (c1_tup[1] + 1)
        if coprime1_pfact:
          c1_tup = coprime1_pfact.pop(0)
        else:
          c1_tup = None
      else:
        div_product = div_product * (c1_tup[1] + c2_tup[1] + 1)
        if coprime2_pfact:
          c2_tup = coprime2_pfact.pop(0)
        else:
          c2_tup = None
        #end if
        if coprime1_pfact:
          c1_tup = coprime1_pfact.pop(0)
        else:
          c1_tup = None
        #end if
      #end if
    #end while
  #end if
  while not c1_tup is None:
    div_product = div_product * (c1_tup[1] + 1)
    if coprime1_pfact:
      c1_tup = coprime1_pfact.pop(0)
    else:
      c1_tup = None

  while not c2_tup is None:
    div_product = div_product * (c2_tup[1] + 1)
    if coprime2_pfact:
      c2_tup = coprime2_pfact.pop(0)
    else:
      c2_tup = None

  if div_product > 500:
    five_hundred_divisors_number = num
  #end if
#end while
print( "%d\n" % five_hundred_divisor_number )

