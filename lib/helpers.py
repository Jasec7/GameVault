from models.console import Console
from models.game import Game


def exit_program():
    print("Goodbye!")
    exit()

def list_consoles():
    consoles = Console.get_all()
    for console in consoles:
        print(f'{console.id}. {console.name}')

def find_console_by_id():
    id_ = input("Enter the console's id:").strip()
    console = Console.find_by_id(id_)
    print(console) if console else print(f'Console {id_} not found')

def create_console():
    name = input("Enter the console's name:")
    try:
        console = Console.create(name)
        print(f"Success: {console.name}")
    except ValueError as exc:
        print("Error creating console:", exc)