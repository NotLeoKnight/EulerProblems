numbers = []
for i in range(1,101):
    numbers.append(i)

numbersSqrd = []
for i in numbers:
    numbersSqrd.append(i**2)

print(sum(numbers)**2 - sum(numbersSqrd))