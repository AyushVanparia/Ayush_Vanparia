number = int(input("Enter Number: "))


if number == 0:
    print("Number is zero")
elif number > 0:
    print("Number is positive")
else:
    print("Number is negative")


print("-----------------------------------------------")
# Ternary Operator

ans = " Number is Even" if number % 2 == 0 else "Number is Odd"
print(ans)
