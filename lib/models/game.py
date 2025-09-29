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
            raise ValueError("console_ide must reference a console in the database")