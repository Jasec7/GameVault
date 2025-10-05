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
            name TEXT  UNIQUE NOT NULL
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """Drop the table that persist Console instances"""
        sql = """
        DROP TABLE IF EXISTS consoles;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Console instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO consoles (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Console instance."""
        sql = """
            UPDATE consoles
            SET name = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql,(self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Console instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM consoles
            WHERE id = ?
        """
        if self.id is not None:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()

        if self.id in type(self).all:
            del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name):
        """Initialize a new Console instance and save it to the database."""
        console = cls(name)
        console.save()
        return console


    @classmethod
    def instance_from_db(cls, row):
        """Return a Console object having the attribute values from the table row"""
        if not row:
            return None

        console = cls.all.get(row[0])
        if console:
            console.name = row[1]
        else:
            console = cls(row[1])
            console.id = row[0]
            cls.all[console.id] = console
        return console

    @classmethod
    def get_all(cls):
        """Return a list containing a Console object per row in the table"""

        sql = """
            SELECT *
            FROM consoles
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls,id):
        """Return a Console object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT * 
            FROM consoles
            WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return Console object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM consoles
            WHERE LOWER(name) = LOWER(?)       
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None



