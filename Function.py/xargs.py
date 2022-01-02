

def addition(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# passing arbitrary arguments
print(addition(10, 20, 30))
