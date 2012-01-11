def d(num):
    div_sum = 1
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            div_sum += i + num/i
    return div_sum

thesum = 0
used_nums = set()
# Saving the results of operations would speed it up a bit..
for i in range(1,10000):
    if i == d(d(i)) and i != d(i):
        if not i in used_nums and d(i) not in used_nums:
            used_nums.add(i)
            used_nums.add(d(i))
            thesum += i + d(i)
print thesum

