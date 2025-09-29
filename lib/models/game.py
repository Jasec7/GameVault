#lib/models/game.py
from models.__init__ import CURSOR, CONN
from models.console import Console

class Game:
    all = {}

    def __init__(self, title, genre, console_id, id = None):
        self.title = title
        self.genre = genre
        self.console_id = console_id
        self.id = id

    def __repr__(self):
        return(
            f"<Game {self.id}: {self.title}, {self.genre}," +
            f"Console ID: {self.console_id}>"
        )

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value.strip()) <= 0:
            raise ValueError("Title must be longer than 0")
        self._title = value

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        if not isinstance(value, str):
            raise ValueError("Genre must be a string")
        if len(value.strip()) <= 0:
            raise ValueError("Genre must be longer than 0")
        self._genre = value

    @property
    def console_id(self):
        return self._console_id
    
    @console_id.setter
    def console_id(self, console_id):
        if type(console_id) is int and Console.find_by_id(console_id):
            self._console_id = console_id
        else:
            raise ValueError("console_id must reference a console in the database")

    @classmethod
    def create_table(cls):
        """Create a new table to persits the attributes of Game instances"""
    sql = """
        CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        console_id INTEGER,
        FOREIGN KEY (console_id) REFERENCES consoles(id))
    """
    CURSOR.execute(sql)
    CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persist Game instances"""
    sql = """
        DROP TABLE IF EXISTS games;
    """
    CURSOR.execute(sql)
    CONN.commit()

    def save(self):
        """ Insert a new row with the title, genre and console_id values of the current Game instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""

    sql = """
            INSERT INTO games (title, genre, console_id)
            VALUES (?,?,?)
    """
    CURSOR.execute(sql,(self.title, self.genre, self.console_id))
    CONN.commit()

    self.id = CURSOR.lastrowid
    type(self).all[self.id] = self    