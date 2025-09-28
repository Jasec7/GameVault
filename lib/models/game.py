#lib/models/game.py
from __init__ import CURSOR, CONN
from console import Console

class Game:
    all = {}

    def __init__(self, title, genre, console_id, id = None):
        self.title = title
        self.genre = genre
        self.console_id = console_id
        self.id = id

    def __repr__(self):
        return(
            f"<Game {self.id}: {self.title}, {self.genre}>"
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