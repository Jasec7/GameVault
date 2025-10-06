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
        for i, console in enumerate(consoles, start = 1):
            print(f'{i}. {console.name}')
    return consoles

def find_console_by_name():
    name =input(Fore.LIGHTMAGENTA_EX +"Enter the console's name: ").strip().title()
    console = Console.find_by_name(name)
    if console:
        print(Fore.YELLOW +f'{console.name}')
        print()
    else:
         print(Fore.RED + f'No console "{name}" was found. Please check the name and try again')

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
    name = input(Fore.LIGHTMAGENTA_EX +"Enter the console's name:").strip().title()
    try:
        console = Console.create(name)
        print(Fore.GREEN + f"Success: {console.name} created")
    except ValueError as exc:
        print(Fore.RED +"Error creating console:", exc)

def update_console(console):
    new_name = input(Fore.LIGHTMAGENTA_EX +f"Enter the console's new name [{console.name}]: ").strip()
    if new_name:
        console.name = new_name
        console.update()
    print(Fore.GREEN +f"Success: updated to {console.name}")

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
    if not games:
        print("No games yet. Press 'A' in the menu to add your first game!")
    else:
        for i, game in enumerate(games, start=1):
            console = Console.find_by_id(game.console_id)
            console_name = console.name if console else "(Unknown Console)"
            print(f'{i}. {game.title} - ({game.genre}) on {console_name}')

def find_game_by_name():
    title =input(Fore.LIGHTMAGENTA_EX +"Enter the game's name: ").strip().title()
    game = Game.find_by_name(title)
    if game:
        console = Console.find_by_id(game.console_id)
        console_name = console.name if console else "(Unknown Console)"
        print(Fore.YELLOW +f'{game.title} - ({game.genre}) on {console_name}')
        print()
    else:
         print(Fore.RED + f'No game "{title}" was found. Please check the name and try again')


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
    title = input(Fore.LIGHTMAGENTA_EX +"Enter the game's title:").strip().title()
    genre = input(Fore.LIGHTMAGENTA_EX +"Enter the game's genre: ").strip().capitalize()
    
    consoles = Console.get_all()
    if not consoles:
        print(Fore.RED + f'No consoles available. Create one first')
        return
    
    print("Select a console for this game:")
    print()
    for i, console in enumerate(consoles, start=1):
        print(Fore.YELLOW + f"{i}. {console.name}")

    choice = input("> ").strip()
    try:
        idx = int(choice)
        selected_console = consoles[idx - 1]
    except (ValueError, IndexError):
        print(Fore.RED + "Invalid selection. Game not created.")
        return
    
    game = Game.create(title, genre, selected_console.id)
    print(Fore.GREEN + f"Success: {game.title} <{game.genre}> on {selected_console.name}")
    
    
def update_game(game):
    new_title = input(Fore.LIGHTMAGENTA_EX +f"Enter new title [{game.title}]: ").strip()
    if new_title:
        game.title = new_title

    new_genre = input(Fore.LIGHTMAGENTA_EX +f"Enter new genre [{game.genre}]: ")
    if new_genre:
        game.genre = new_genre

    game.update()
    print(Fore.GRENN +f"Success: updated to {game.title}")

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