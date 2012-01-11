
def divisors(num):
    divisors = set([1])
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num/i)

    return divisors

MAX_NUM = 28123

abnums = [i for i in range(1, MAX_NUM) if sum(divisors(i)) > i]
sums = []
for i, num in enumerate(abnums):
    for num2 in abnums[i:]:
        sums.append(num+num2)


allnums = set(range(MAX_NUM))
print sum(allnums.difference(sums))
