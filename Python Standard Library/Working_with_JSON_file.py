import json
from pathlib import Path
# writing json file
# cars = [
#     {"company": "tata", "name": "hexon"},
#     {"company": "suzuki", "name": "swift"},
#     {"company": "renault", "name": "kwid"}
# ]

# data = json.dumps(cars)

data = Path("JSON_Example.json").read_text()
movies = json.loads(data)
print(movies)
