import sys
import math

n = int(sys.stdin.readline().strip())

inputs = []
for i in range(n):
  num = int(sys.stdin.readline().strip())
  inputs.append(num)

def sieve(n):
  isPrime = [True] * (n + 1)
  isPrime[0] = False
  for i in range(2, int(n**0.5) + 1):
    if isPrime[i]:
      for j in range(i*i, n + 1, i):
        isPrime[j] = False
  return isPrime

primes_list = sieve(max(inputs) * 2)

for val in inputs:
  target = val * 2
  for p in range(2, target):
    if primes_list[p] and primes_list[target - p]:
      print(p, target - p)
      break