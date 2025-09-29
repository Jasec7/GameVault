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
    id_str = input("Enter the console's id: ").strip()
    try:
        id_ = int(id_str)   # convert to int
    except ValueError:
        print("Error: id must be a number")
        return

    console = Console.find_by_id(id_)
    print(console) if console else print(f'Console {id_} not found')

def create_console():
    name = input("Enter the console's name:").strip()
    try:
        console = Console.create(name)
        print(f"Success: {console.name} created")
    except ValueError as exc:
        print("Error creating console:", exc)

def update_console():
    id_str = input("Enter the console's id: ").strip()
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: id must be a number")
        return
    
    if console := Console.find_by_id(id_):
        try:
            name = input("Enter the console's new name: ")
            console.name = name
            console.update()
            print(f'Success: {console}')
        except ValueError as exc:
            print("Error updating console: ", exc)
    else:
        print(f"Console {id_} not found")

def delete_console():
    id_str = input("Enter the console's id: ").strip()
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: id must be a number")
        return

    if console := Console.find_by_id(id_):
        console.delete()
        print(f"Console {console.name} deleted")
    else:
        print(f"Console {id_} not found")