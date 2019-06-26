import math

n = int(input('n: '))

sieve = [True] * (n + 1)

for i in range(2, int(math.sqrt(n) + 1)):
    if sieve[i]:
        j = i * i
        while j < (n + 1):
            sieve[j] = False
            j += i

print(sieve)
