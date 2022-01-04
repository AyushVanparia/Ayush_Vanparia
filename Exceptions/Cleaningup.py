try:
    file = open("Cleaning.py")
    a = int(input("Enter Number: "))
    y = 10/a
except (ValueError, ZeroDivisionError):
    print("Enter valid number")
finally:  # it will be executed whether their is exception or not0
    file.close()
