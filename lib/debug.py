#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.console import Console
#from models.game import Game
#import ipdb


Console.drop_table()
Console.create_table()


c1 = Console("PS5")
print(c1)

c2 = Console("   ")  
