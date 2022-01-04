def calculate(age):
    if age <= 0:
        raise ValueError("Age cannot be zero")
    return 10/age


try:
    calculate(-1)
except ValueError as exp:
    print(exp)
