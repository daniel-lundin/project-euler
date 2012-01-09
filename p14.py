
cache = {}
def sequence_len(seed):
    pass
    curr_len = 1
    curr = seed
    while curr != 1:
        if curr % 2 == 0:
            curr = curr/2
        else:
            curr = 3*curr + 1
        curr_len += 1
        if curr in cache:
            tot_len =  curr_len + cache[curr]
            cache[seed] = tot_len
            return tot_len
    cache[seed] = curr_len
    return curr_len

longest=0
longest_seed=0
for i in range(1,1000000):
    length = sequence_len(i)
    if length > longest:
        longest = length
        longest_seed = i
print "Seed %d gives a length of %d" % (longest_seed, longest)

