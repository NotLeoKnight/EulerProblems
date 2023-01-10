evenFibonacci = []

def sequence(fibonacci_before = 0, fibonacci_after = 0):
    fibonacci_final = fibonacci_before + fibonacci_after
    if fibonacci_final >= 4_000_000:return
    if fibonacci_final % 2 == 0: evenFibonacci.append(fibonacci_final)
    sequence(fibonacci_after=fibonacci_final, fibonacci_before=fibonacci_after)

sequence(fibonacci_after=1, fibonacci_before=0)
print(sum(evenFibonacci))