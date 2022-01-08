from datetime import datetime
import time


dt1 = datetime(2021, 4, 12)
dt2 = datetime.now()
print(dt2)
print(dt2 > dt1)
#  strptime() converts a string into date datetime object
dt3 = datetime.strptime("2022/12/31", "%Y/%m/%d")
dt4 = datetime.fromtimestamp(time.time())
dt5 = dt3.strftime("%d-%m-%Y")  # converts a datetime obj to string
print(dt5)
