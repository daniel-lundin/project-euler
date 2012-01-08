import math

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

p = prime_generator()
[p.next() for _ in range(10000)]
print p.next()
