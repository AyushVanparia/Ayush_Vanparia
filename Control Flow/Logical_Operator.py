# and - Returns True if Both condtions are true
""" a = int(input("Enter number: "))
b = int(input("Enter number: "))


if a > 0 and b >0:
    print("Both are greater than zero")
else:
    print("One of the number is less than zero") """

# ------------------------------------------------------------
# or - returns true if one of the condition is true


""" user_name = input("Enter UserName: ")
password = input("Enter Password: ")

if user_name == "admin" or password == "qwer":
    print(f"Welcome {user_name}")
else:
    print("Invalid Password or username") """

# ------------------------------------------------------------

# not - returns true is condition is false
password = input("Enter Password: ")

if not password == "qwer":
    print("Invalid Password")
else:
    print("hello")
