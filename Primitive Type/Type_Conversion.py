# input() to take value from user
a = input("a :")
# type() returns type of variable
print(type(a))
# int() is used to convert a variable into integer
# float() is used to convert a variable into float
# str() is used to convert a variable into string
# bool() is used to convert a variable into boolean

b = int(a)
print(f"before conversion {type(a)}, after conversion {type(b)}")

# in bool() anything except1
# ""
# 0
# none
# will return true

c = bool(0)
print(c)
d = bool(3)
print(d)
