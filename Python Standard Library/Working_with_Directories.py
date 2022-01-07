from pathlib import Path

path1 = Path(r"E:\Devops\Ayush_Vanparia\Modules\Packages")
print(path1.exists())
# path1.mkdir()  # to make directory
# path1.rmdir()# to remove directory
# print(path1.rename(r"E:\Devops\Ayush_Vanparia\Modules\Packages"))
# is_dir checks it is directory or not
# iterdir give the list of diretories and file in a path, returns generator expression
p1 = [p for p in path1.iterdir() if p.is_dir()]
# give file according to pattern, returns genertor expression
#p2 = [p1 for p1 in path1.glob("*.py")]
print("--------------------------------------------")
# to search recurcively recursively, returns all the files according the pattern in the path
p2 = [p for p in path1.rglob("*.py")]
print(p2)
