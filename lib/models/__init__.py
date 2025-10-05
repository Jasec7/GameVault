import sqlite3

CONN = sqlite3.connect('gamevault.db')
CURSOR = CONN.cursor()
CONN.execute("PRAGMA foreign_keys = ON;")

