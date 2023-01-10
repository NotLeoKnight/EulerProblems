multiples = []
for  i in range(0,1000):
    if i % 5 == 0 or i % 3 == 0:
        multiples.append(i)

print(sum(multiples))