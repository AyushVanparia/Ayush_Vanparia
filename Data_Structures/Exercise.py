sentence = "this is sparta"

dict1 = {}

for char in sentence:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

sort = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
print(sort[0])
