# Takes 7 s on my laoptop

divisors = range(20,0,-1)
def even_divisable(num):
    for divisor in divisors:
        if num%divisor != 0:
            return False
    return True

num=20
while not even_divisable(num):
    num += 20

print num

