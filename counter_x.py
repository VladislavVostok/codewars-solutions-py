def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [z for z in range(x, x*n + 1) if z % x == 0]
    return [z for z in range(x, x*n + 1)][::x]

print(count_by(1, 5))
print(count_by(50, 5))
print(count_by(2, 5))