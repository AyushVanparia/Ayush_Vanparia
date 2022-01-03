# tup1 = (1, 2, 3)  # simple tuple

# tup2 = (1,)  # single value tuple add coma after item otherwise it will take it as int
# print(type(tup2))

# concatinating tuple
#tup1 = (1, 2) + (3, 4)

# or

# tup1 = (1, 2)*3

# creating tuple with tuple method
# tup1 = tuple("helllo world")

# accessing tuple items
#tup1 = tuple(range(5))
# print(tup1[:4])

# packing tuple
tup1 = tuple(range(10))
first, *other, last = tup1
print(first, last)
print(other)
