import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("JSON_Example.json").read_text())
with sqlite3.connect("Abc.sqlite3") as conn:
    command = "insert into def values(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
