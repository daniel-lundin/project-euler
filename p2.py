def fib_gen():
    """ Fibonacci generator for numbers less than 4 million"""
    yield 1
    yield 2
    a,b = 1, 2
    while a+b<4000000:
        yield a+b
        a,b=b,a+b

g = fib_gen()
def sum_if_even(a,b):
    return a * ((a-1) % 2) + b * ((b-1) % 2)
even_sum = reduce(sum_if_even, g)
print "Sum is: ", even_sum
