#from Module import fname, lname
# # or
# import Module


# fname()
# lname()

# print("----------------------")

# Module.fname()
# Module.lname()

# -------------------------------------------------------
from Packages.Sub_Package.Module import fname, lname
from Packages.Sub_Package import Module
# -----------------------------------------------
from Packages import Module2

Module.fname()
Module.lname()

print("--------------------------------------")

Module2.mod1()
Module2.mod2()
