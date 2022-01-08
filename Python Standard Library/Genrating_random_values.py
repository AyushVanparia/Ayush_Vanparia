import random
import string

print(random.random())  # generates random values between 0 and 1
# .randint() generates random values between given int numbers
print(random.randint(1, 10))
# .choise() takes an array and randomly select number from that array
print(random.choice([1, 2, 3, 4, 5]))
# .choises() takes an array and randomly select multiple number from that array
print(random.choices("abdefghijk", k=4))
print("".join(random.choices(string.ascii_letters +
      string.digits+string.punctuation, k=4)))

num = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(num)
print(num)
