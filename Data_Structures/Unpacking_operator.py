lst1 = list(range(10))
print(*lst1)

dict1 = {"first": 1, "second": 2}
dict2 = {"fi": 2}
dict3 = {**dict1, **dict2, "z": 4}
print(dict3)
