try:
    a = int(input("Enter number: "))
    y = 10/a
except (ValueError, ZeroDivisionError):
    print("Enter valid number ")
else:
    print("no exceptions were thrown")
