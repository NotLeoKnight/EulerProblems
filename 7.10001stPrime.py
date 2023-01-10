primes = []
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )

current = 1
while len(primes) <= 10_001:
    if is_prime(current): primes.append(current)
    current +=2

print(primes[len(primes)-1])