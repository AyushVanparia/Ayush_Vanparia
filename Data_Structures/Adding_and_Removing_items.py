lst1 = list("abcdefghji")
print(lst1)
print("-------------------------------------")

# Adding item
# 1. append() method will add item at the last in list
lst1.append("k")
# 2. insert() method will add item at the starting of the list(by default) or we can specify index number to add item
lst1.insert(2, "+++")
print(lst1)
print("-------------------------------------")

# removing item
# 1. pop() method will remove last item in list(by default) or we can specify index numberto remove item
lst1.pop(2)
# 2. remove() passing item we want to remove we can remove item
lst1.remove("k")
# 3.del will delete entire list(by default)or we can sepcify index number to remove item or we can delete in by slicing
del lst1[3:]
print(lst1)
print("-------------------------------------")
# 4. clear() will clear entier list
lst1.clear()
print(lst1)
