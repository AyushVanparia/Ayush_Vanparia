lst1 = [
    ("position 1", 4),
    ("position 2", 3),
    ("position 3", 2)
]

lst2 = list(filter(lambda item: item[1] >= 3, lst1))

print(lst2)
