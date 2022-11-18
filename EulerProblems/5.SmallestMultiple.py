multiples = []
def isDevisable(num):
    for i in range(1,21):
        if num % i != 0: return False
    return True

for num in range(2520, 1_000_000_000, 2520):
    if isDevisable(num): multiples.append(num)


print(multiples)