#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.console import Console
from models.game import Game
from helpers import create_console
from helpers import find_console_by_name
from helpers import list_games
from helpers import find_game_by_id
from helpers import update_game
from helpers import list_consoles
#import ipdb

Game.drop_table()
Console.drop_table()
Console.create_table()
Game.create_table()


c1 = Console("PS5")
c1.save()
print(c1)

c1.name = "Play Station 5"
c1.update()
print(c1)

c2 = Console("Nintendo switch")
c2.save()
print(c2)

#c1.delete()
#print(c1)

#print(Console.find_by_id(c1.id))
#print(Console.find_by_id(999))
#print(Console.get_all())

g1 = Game("Metal Gear Solid", "action", c1.id)
g2 = Game("Zelda", "adventure", c2.id)
g3 = Game("Tetris", "puzzle" , c1.id)
g3.save()
g2.save()
g1.save()
#print(g1)
#print(g2)
#print(g3)

#g2.delete()
#print(g2)

#print(Game.find_by_id(g1.id))
#print(Game.find_by_id(22))
#print(Game.get_all())

#create_console()
list_games()
#find_console_by_name()
#find_game_by_id()
#update_game()
list_consoles()