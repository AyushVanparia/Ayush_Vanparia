import csv
from os import write
# writing csv file
with open("csv_example.csv", "w") as file:
    obj = csv.writer(file)
    obj.writerow(["no", "name", "salary"])
    obj.writerow(["1", "raj", "45000"])
    obj.writerow(["2", "deep", "55000"])

# reading csv file
with open("csv_example.csv") as file:
    obj = csv.reader(file)
    for row in obj:
        print(row)
