# defining dictionary
dict1 = {"a": 1, "b": 2}
print(f"dict1 = {dict1}")
dict2 = dict(a=1, b=2)
print(f"dict2 = {dict2}")

# accessing dictionay
print(dict1["a"])

#  adding key
dict1["c"] = 3
print("After adding")
print(f"dict1 = {dict1}")

# deleting
del dict1["c"]
print("After deleting")
print(f"dict1 = {dict1}")

# iterating over dictionary
for x, y in dict1.items():
    print(x, y)
