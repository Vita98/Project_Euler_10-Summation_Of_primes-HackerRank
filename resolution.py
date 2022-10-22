#!/bin/python3

import sys

primes = []
sums = {}

# Generating the primes with the sieve of eratosthenes
def generatePrimes(n):
    allNumbers = list(range(2,n+1))
    numbDict = {}
    
    for m in allNumbers:
        numbDict[m] = True
        
    for m in allNumbers:
        if numbDict[m] == False:
            sums[m] = sums[m-1]
            continue
        
        primes.append(m)
        
        if not sums:
            sums[m] = m
        else:
            sums[m] = sums[m-1]+m
        
        #remove all multiples
        k = 2
        while k*m <= n:
            numbDict[k*m] = False
            k += 1

    
    
def solve(n):
    return sums[n]

t = int(input().strip())
ns = []
maxN = 0
for a0 in range(t):
    n = int(input().strip())
    ns.append(n)
    if n > maxN:
        maxN = n
        
generatePrimes(maxN)

for n in ns:
    print(solve(n))