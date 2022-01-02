def my_power(base, pow=2):  # here pow is made default parameter by assigning it a value at the time of declaration
    ans = 1
    for i in range(pow):
        ans *= base
    return ans


# if the second argument is not given it will take 2 as the value of pow
print("With one arument")
print(my_power(3))

print("With two argument")
print(my_power(3, 5))
