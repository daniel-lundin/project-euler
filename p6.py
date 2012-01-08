sum_of_squares = sum(map(lambda x: x*x, range(1, 101)))
sums = sum(range(1, 101))
square_of_sums = sums*sums
print square_of_sums - sum_of_squares
