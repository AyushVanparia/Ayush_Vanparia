def my_function(**student):
    print(student["fname"])
    print(student["lname"])
    print(student["age"])
    print(student)


my_function(fname="Ayush", lname="Vanparia", age=19)
