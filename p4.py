def is_palinumber(num):
    snum = str(num)
    for i in range(len(snum)/2):
        if snum[i] != snum[-(i+1)]:
            return False
    return True

largest=0
for i in range(1000,1,-1):
    for j in range(i,1,-1):
        if is_palinumber(i*j):
            largest = max(largest, i*j)
print largest
