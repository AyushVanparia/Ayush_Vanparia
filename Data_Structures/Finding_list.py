lst1 = list("abcdd")
# by using in operator we can check if specific item exists in list or not
# iindex will return the index number of specified item
print(lst1.count("d"))  # will return the number occurences of specified item
if "e" in lst1:
    print(lst1.index("e"))
