from pathlib import Path
from time import ctime
import shutil
path1 = Path(
    r"E:\Devops\Ayush_Vanparia\Python Standard Library\testpack\for_testing.py")
pastefile = Path(
    r"E:\Devops\Ayush_Vanparia\Python Standard Library\testpack\another.py")
print(path1.exists())
print(pastefile.exists())
# # path1.rename("E:\Devops\Ayush_Vanparia\Modules\Packages\Module3.py")
# # path1.unlink() # to delete file
# print(path1.stat())  # returns information about file
# # ctime returns the creatio time in human readable language
# print(ctime(path1.stat().st_ctime))
# print(path1.read_text())  # returns the content of the file in string
# path1.write_text("#file edited")

# shutil module's copy function can be used to copy a file amd paste to another file
shutil.copy(path1, pastefile)
