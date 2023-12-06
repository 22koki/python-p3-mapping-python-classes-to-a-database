import os
import sqlite3

# Get the absolute path to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'lib', 'music.db')

CONN = sqlite3.connect('/home/fay/python-p3-mapping-python-classes-to-a-database/lib/music.db')
CURSOR = CONN.cursor()

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.lastrowid  # Use lastrowid on the cursor

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

# Create the songs table
Song.create_table()

# Create and save songs
hello = Song.create("Hello", "25")
despacito = Song.create("Despacito", "Vida")

# Accessing attributes
print(hello.id)         # => 1
print(despacito.id)     # => 2
print(hello.name)       # => "Hello"
print(despacito.album)  # => "Vida"
