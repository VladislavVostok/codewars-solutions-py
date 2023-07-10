def descending_order(num):
    return int("".join(sorted([ i for i in str(num)])[::-1]))

print(descending_order(123456789))
print(descending_order(0))
print(descending_order(15))