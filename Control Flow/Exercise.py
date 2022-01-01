# to print even number between 1 to 10 and how many are there
even_number = 0
for i in range(1, 10):
    if(i % 2 == 0):
        print(i)
        even_number += 1

print(f"there are {even_number} even number")
