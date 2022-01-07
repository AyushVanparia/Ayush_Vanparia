from pathlib import Path

path1 = Path(
    r"E: \Devops\Ayush_Vanparia\PythonStandardLibrary\testpack\for_testing.py")
print(path1)
print(path1.exists())
print(path1.name)  # returns file name in the path
print(path1.stem)  # returns file name in the path not extension
print(path1.suffix)  # returns extension of the path
print(path1.parent)  # returns the parent of the file
#path2 = path1.with_name("file.text")
path2 = path1.with_suffix(".txt")
print(path2)
print(path1.absolute())
