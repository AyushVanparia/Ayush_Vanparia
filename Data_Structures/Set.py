# creating set
lst1 = [1, 1, 2, 3, 4]
set1 = set(lst1)
print(f"set1 = {set1}")
set2 = {1, 5}
print(f"set2 = {set2}")

#  union of two set
print(f"Union = {set1 | set2}")

# intersection of two set
print(f"Intersection = {set1 & set2}")

# difference of two set
print(f"Difference = {set1 - set2}")

# symetric difference
print(f"Symetric difference = {set1 ^ set2}")
