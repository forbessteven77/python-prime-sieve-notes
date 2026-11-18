import math

def sieve(limit):
    if limit < 2:
        return []
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            for multiple in range(p*p, limit+1, p):
                prime[multiple] = False
    return [i for i, flag in enumerate(prime) if flag]

def solve(value):
    return sieve(value)
