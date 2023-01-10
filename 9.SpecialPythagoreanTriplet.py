
def findTriplet():                 
    for a in range(1,1000):
        for b in range(0,1000-a):
            c = (1000-a)-b
            if a**2 + b**2 == c**2: 
                if a + b + c == 1000: 
                    print(f"FOUND IT: {a,b,c} | {a+b+c}")
                    return


findTriplet()