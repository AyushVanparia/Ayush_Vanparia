for i in range(1, 10, 2):
    if i == 12:
        print("found")
        break
    # here else will execute if for loop is compeletely executed, without any early termination
else:
    print("not found")
