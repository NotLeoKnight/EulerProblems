primes = []
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )

current = 1_000_001
while True:
    if is_prime(current): 
        if current >= 2_000_000: break
        primes.append(current)
    current +=2

print(primes[len(primes)-1])