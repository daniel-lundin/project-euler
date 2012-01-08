import math

bignumber=600851475143

def prime_generator():
    i = 2
    while True:
        is_prime = True
        for j in range(2,int(math.sqrt(i))+1):
            if (i % j) == 0:
                is_prime = False
                continue
        if is_prime:
            yield i
        i+=1

p=prime_generator()
pfs = []
while p:
    prime = p.next()
    if bignumber % prime == 0:
        pfs.append(prime)
        if reduce(lambda a,b: a*b, pfs) == bignumber:
            print "Largest prime", prime
            exit(0)

