import sqlite3
import json
from pathlib import Path
from sqlite3.dbapi2 import Cursor


with sqlite3.connect("Abc.sqlite3") as conn:
    command = "select * from def"
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    # conn.commit()
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
