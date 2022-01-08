from datetime import datetime, timedelta

dt1 = datetime(2021, 1, 8) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)

print("days", duration.days)
print("seconds", duration.seconds)
print("total seconds: ", duration.total_seconds())
