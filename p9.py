import math

def is_pyth_triplet(a,b,c):
    return a*a + b*b == c*c

def sums_to_1000(a,b,c):
    return a+b+c==1000

for a in range(1,1000):
    for b in range(a,1000):
        c = int(math.sqrt(a*a + b*b))
        if is_pyth_triplet(a,b,c) and sums_to_1000(a,b,c):
            print "Product a*b*c: ", a*b*c
