from models.console import Console
from models.game import Game


def exit_program():
    print("Goodbye!")
    exit()

def list_consoles():
    consoles = Console.get_all()
    for console in consoles:
        print(f'{console.id}. {console.name}')

def find_console_by_name():
    name =input("Enter the console's name: ").strip()
    console = Console.find_by_name(name)
    print(console) if console else print(f"No console {name} was found. Please check the name and try again")

def find_console_by_id():
    id_str = input("Enter the console's id: ").strip()
    try:
        id_ = int(id_str)   
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
            name = input("Enter the console's new name: ").strip()
            console.name = name
            console.update()
            print(f'Success: update to {console}')
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

    
def list_games():
    games = Game.get_all()
    for game in games:
        console = Console.find_by_id(game.console_id)
        print(f'{game.id}. {game.title} - ({game.genre}) on {console.name}')

def find_game_by_name():
    name =input("Enter the game's name: ").strip()
    game = Game.find_by_name(name)
    print(game) if game else print(f"No game {name} was found. Please check the name and try again")

def find_game_by_id():
    id_str = input("Enter the game's id: ").strip()
    try:
        id_ = int(id_str)   
    except ValueError:
        print("Error: id must be a number")
        return

    game = Game.find_by_id(id_)
    print(game) if game else print(f'Game {id_} not found')

def create_game():
    title = input("Enter the game's title:").strip().capitalize()
    genre = input("Enter the game's genre: ").capitalize()
    console_id = input("Enter the console's id: ")
    try:
        console_id = int(console_id)
        game = Game.create(title, genre, console_id)
        print(f"Success: {game.title} created")
    except ValueError as exc:
        print("Error creating game:", exc)

def update_game():
    id_str = input("Enter the game's id: ").strip()
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: id must be a number")
        return
    
    if game := Game.find_by_id(id_):
        try:
            title = input("Enter the game's new title: ").capitalize()
            game.title = title
            genre = input("Enter the game's new genre: ").capitalize()
            game.genre = genre
            console_id = input("Enter the console's new id: ")
            game.console_id = int(console_id)

            game.update()
            print(f'Success: updated to {game}')
        except ValueError as exc:
            print("Error updating game: ", exc)
    else:
        print(f"Game {id_} not found")

def delete_game():
    id_str = input("Enter the game's id: ").strip()
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: id must be a number")
        return

    if game := Game.find_by_id(id_):
        game.delete()
        print(f"Game {game.title} deleted")
    else:
        print(f"Game {id_} not found")