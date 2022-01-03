lst1 = list(range(15))
# list unpacking
first, second, *other, last = lst1

print(first, second, last)
print(other)
print(f"type of other :{type(other)}")
