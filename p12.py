
def triangle_num_generator():
    i = 1
    while True:
        yield sum(range(i + 1))
        i += 1

#TODO: Use prime factors and num-of-divisors function instead 

def count_divisors(num):
    num_divisors = 2 if num != 1 else 1 # always dividable by 1 and itself
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            num_divisors += 2
    return num_divisors

g = triangle_num_generator()
curr_trinum = g.next()

while not count_divisors(curr_trinum) > 500:
    curr_trinum = g.next()

print curr_trinum 

