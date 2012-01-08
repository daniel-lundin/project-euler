import math

def prime_generator(n):
    yield 2
    i = 3
    while i<n:
        is_prime = True
        j = 3
        isq = int(i ** 0.5)
        while j <= isq:
            if i % j == 0:
                is_prime = False
                break
            j += 2
        if is_prime:
            yield i
        i+=2

p = prime_generator(2000000)
print sum(p)
