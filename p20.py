def fak(n):
    if n == 0:
        return 1
    return n*fak(n-1) 

print sum([int(x) for x in str(fak(100))])
