primes = []
def Prime_series(number):
    for i in range(2,number):
        if is_prime(i) == True:
            primes.append(i)
        else:
            pass

is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
Prime_series(10000)
num = 600851475143

factors = []
while True:
    for prime in primes:
        if num % prime == 0 : 
            num = num / prime
            factors.append(prime)
    if num == 1 :break
print(factors)