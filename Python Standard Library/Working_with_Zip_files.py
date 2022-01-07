from pathlib import Path
from zipfile import ZipFile

# with ZipFile("Zip_example.zip", "w") as zip1:
#     for path in Path("E:\Devops\Ayush_Vanparia\Python Standard Library").rglob("*.*"):
#         zip1.write(path)


with ZipFile("Zip_example.zip") as zip2:
    print(zip2.namelist())  # returns the list of file and dictionaries in zip
    info = zip2.getinfo(
        "Devops/Ayush_Vanparia/Python Standard Library/testpack/another.py")  # get the info file from zip
    print(info)
    print(info.file_size)  # get the  size  of file in the zip
    print(info.compress_size)  # get the compress size of file in the zip
    # to extract file from zip
    zip2.extractall("extract")
