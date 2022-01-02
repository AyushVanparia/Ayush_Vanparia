""" nm = input("Enter Name: ")

# without return


def info(name):

    print(f"hello {name}")


info(nm) """
# with return

a = int(input("Enter Number: "))
b = int(input("Enter Number: "))


def addition(x, y):

    add = x + y
    return add


ans = addition(a, b)

print(ans)
