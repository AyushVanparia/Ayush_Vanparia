string1 = "     hello this is python programming"
# upper() convert whole String in upper case.
print(string1.upper())
# lower() Converts whole string to lower case.
print(string1.lower())
# title() converts every first letter of every word in string  to capital.
print(string1.title())
# strip() removes whitespace from the beginning and from end of the code.
print(string1.strip())
# find() is used to find index number of  given character or sequence of character.
#  gives -1 if character or sequence of character is not found.
print(string1.find("t"))
# replace() is used to replace character or sequence of character.
# first give character or sequence of character you want to replace with and second give character you want.
print(string1.replace("py", "ja"))
# checks the given value is present in string. Returns true if  value exists.
print("hello" in string1)
# checks the given value is not present in string. Returns true is if vale does not exists.
print("helo" not in string1)
