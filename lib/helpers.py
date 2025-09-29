from models.console import Console
from models.game import Game


def exit_program():
    print("Goodbye!")
    exit()

def list_consoles():
    consoles = Console.get_all()
    for console in consoles:
        print(console) 