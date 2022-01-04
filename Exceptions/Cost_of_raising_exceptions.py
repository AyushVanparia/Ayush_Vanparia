from timeit import timeit


code1 = """ 
def calculate(age):
    if age <= 0:
        raise ValueError("Age cannot be zero")
    return 10/age


try:
    calculate(-1)
except ValueError as exp:
    print(exp)
 """

code2 = """ 
def calculate(age):
    if age <= 0:
        return None
    return 10/age
calculate(-1)


 """

# timeit() function we can calculate execution time of python code
print("first code", timeit(code1, number=10000))
print("Second code", timeit(code2, number=10000))
