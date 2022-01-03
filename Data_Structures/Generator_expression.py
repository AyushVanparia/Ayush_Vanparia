from sys import getsizeof

val1 = (x*2 for x in range(10000))
print(getsizeof(val1))

val2 = [x*2 for x in range(10000)]
print(getsizeof(val2))
# print(len(val1))
