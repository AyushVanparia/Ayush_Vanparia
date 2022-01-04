try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Invalid age, please enter your age again")
    print(ex)
    print(type(ex))
else:  # it will be executed when there is no execution
    print("No exception occured")
print("Execution continues")
