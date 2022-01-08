import sys

if len(sys.argv) == 1:
    print("USAGE: python3 Command_Line_Argument.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
