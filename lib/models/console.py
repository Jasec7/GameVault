# lib/models/console.py
from models.__init__ import CURSOR, CONN

class Console:
    all = {}

    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"<Console {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value.strip()) <= 0:
            raise ValueError("Console name must be longer than 0")
        self._name = value
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Console instances """
        sql = """
            CREATE TABLE IF NOT EXISTS consoles (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
