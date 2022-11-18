def isPalendrome(num):
    digits = list(str(num))
    revDigits = digits[::-1]
    if digits == revDigits: return True

palendromes = []
for i in range(100*100, 999*999):
    if isPalendrome(i): palendromes.append(i)

print(palendromes[len(palendromes)-1])