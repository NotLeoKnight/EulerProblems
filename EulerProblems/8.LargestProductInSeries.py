import json

with open("data.json") as f:
    data = json.load(f)
    number1000 = str(data["LargestProductInSeries"])

products = []
multiples = []

current = 0
while True:

    for i in number1000[current:current+13]:
        products.append(int(i))
    multiples.append(sum(products))

    if current < 987: current += 1
    else: break    

print(max(multiples))