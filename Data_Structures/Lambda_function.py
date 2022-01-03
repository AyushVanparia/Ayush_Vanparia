lst2 = [
    ("position 1", 4),
    ("position 2", 3),
    ("position 3", 2)
]

lst2.sort(key=lambda item: item[1])

print(lst2)
