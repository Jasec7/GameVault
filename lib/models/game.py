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
        """Create a new table to persist the attributes of Game instances"""
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

    def update(self):
        """Update the table row corresponding to the current Game instance."""

        sql = """
            UPDATE games
            SET title = ?, genre = ?, console_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.genre, self.console_id, self.id))
        CONN.commit()

    
    def delete(self):
        """Delete the table row corresponding to the current Game instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM games
            WHERE id = ?
        """

        if self.id is not None:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()

        if self.id in type(self).all:
            del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Game object having the attribute values from the table row"""
        if not row:
            return None

        game = cls.all.get(row[0])
        if game:
            game.title = row[1]
            game.genre = row[2]
            game.console_id = row[3]
        else:
            game = cls(row[1], row[2], row[3])
            game.id = row[0]
            cls.all[game.id] = game
        return game

    @classmethod
    def get_all(cls):
        """Return a list containing a Game object per row in the table"""

        sql = """
            SELECT *
            FROM consoles
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]