lst1 = [
    ("position 1", 4),
    ("position 2", 3),
    ("position 3", 2)
]


lst2 = list(map(lambda item: item[1], lst1))
lst3 = [item[1] for item in lst1]
print(lst3)

lst4 = list(filter(lambda item: item[1] >= 3, lst1))
lst5 = [item for item in lst1 if item[1] >= 3]
print(lst4)
