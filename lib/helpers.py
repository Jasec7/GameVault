from models.console import Console
from models.game import Game
from colorama import Fore, Style, init
init(autoreset=True)


def exit_program():
    print(Fore.GREEN +"Goodbye Gamer!")
    exit()


def list_consoles():
    consoles = Console.get_all()
    if not consoles:
        print("No consoles yet. Try adding one!")
    else:
        for console in consoles:
            print(f'{console.id}. {console.name}')
    return consoles

def find_console_by_name():
    name =input("Enter the console's name: ").strip()
    console = Console.find_by_name(name)
    print(console) if console else print(Fore.RED +f'No console "{name}" was found. Please check the name and try again')

def find_console_by_id():
    id_str = input("Enter the console's id: ").strip()
    try:
        id_ = int(id_str)   
    except ValueError:
        print(Fore.RED +"Error: id must be a number")
        return

    console = Console.find_by_id(id_)
    print(console) if console else print(f'Console {id_} not found')

def create_console():
    name = input("Enter the console's name:").strip().title()
    try:
        console = Console.create(name)
        print(Fore.GREEN + f"Success: {console.name} created")
    except ValueError as exc:
        print(Fore.RED +"Error creating console:", exc)

def update_console(console):
    new_name = input(f"Enter the console's new name [{console.name}]: ").strip()
    if new_name:
        console.name = new_name
        console.update()
    print(Fore.YELLOW +f"Success: updated to {console.name}")

def delete_console():
    id_str = input("Enter the console's id: ").strip()
    try:
        id_ = int(id_str)
    except ValueError:
        print(Fore.RED +"Error: id must be a number")
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
    title =input("Enter the game's name: ").strip().title()
    game = Game.find_by_name(title)
    print(game) if game else print(Fore.RED +f'No game "{title}" was found. Please check the name and try again')

def find_game_by_id():
    id_str = input("Enter the game's id: ").strip()
    try:
        id_ = int(id_str)   
    except ValueError:
        print(Fore.RED +"Error: id must be a number")
        return

    game = Game.find_by_id(id_)
    print(game) if game else print(f'Game "{id_}" not found')

def create_game():
    title = input("Enter the game's title:").strip().title()
    genre = input("Enter the game's genre: ").strip().capitalize()
    console_id = input("Enter the console's id: ")
    try:
        console_id = int(console_id)
        game = Game.create(title, genre, console_id)
        print(Fore.GREEN + f"Success: {game.title} created")
    except ValueError as exc:
        print(Fore.RED +"Error creating game:", exc)

def update_game(game):
    new_title = input(Fore.YELLOW +f"Enter new title [{game.title}]: ").strip()
    if new_title:
        game.title = new_title

    new_genre = input(Fore.YELLOW +f"Enter new genre [{game.genre}]: ")
    if new_genre:
        game.genre = new_genre

    game.update()
    print(Fore.YELLOW +f"Success: updated to {game.title}")

def delete_game():
    id_str = input("Enter the game's id: ").strip()
    try:
        id_ = int(id_str)
    except ValueError:
        print(Fore.RED +"Error: id must be a number")
        return

    if game := Game.find_by_id(id_):
        game.delete()
        print(f"Game {game.title} deleted")
    else:
        print(Fore.RED +f"Game {id_} not found")