"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largest_prime_fac(n):
  if n < 1:
    raise ValueError('Number is less than 1')
  if n == 1:
    return 1

  largest = 0
  i = 2
  while i <= n:
    if n % i == 0:
      largest = i
      n = n / i
    else:
      i += 1
  return largest

print(largest_prime_fac(600851475143))
