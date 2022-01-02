num = int(input("Enter Number: "))


def fizz_buzz(no):

    if no % 3 == 0 and no % 5 == 0:
        return "FizzBuzz"
    else:
        if no % 3 == 0:
            return "Fizz"
        elif no % 5 == 0:
            return "Buzz"

    return no


print(fizz_buzz(num))
