from colorama import Fore, Style, init
from models.console import Console
from models.game import Game
init(autoreset=True)

from helpers import (
    exit_program,
    list_consoles,
    find_console_by_name,
    find_console_by_id,
    create_console,
    update_console,
    delete_console,
    list_games,
    find_game_by_name,
    find_game_by_id,
    create_game,
    update_game,
    delete_game
)


def main():
    while True:
        print(Fore.GREEN + "Welcome to GameVault!")
        print(Fore.CYAN + "*** Main Menu ***")
        print(Fore.YELLOW +"Type the letter from the following options:")
        print(Fore.YELLOW +"C. Consoles")
        print(Fore.YELLOW +"G. Games")
        print(Fore.YELLOW +"E. Exit")

        choice = input("> ").strip().lower()
        if choice == "e":
            exit_program()
        elif choice == "c":
            consoles_menu()
        elif choice == "g":
            games_menu()
        else: 
             print(Fore.RED +"Invalid choice, please try again.")



def consoles_menu():

    while True:
        print(Fore.CYAN + "*** Consoles Menu ***")
        print(Fore.YELLOW +"1. List all consoles")
        print(Fore.YELLOW +"2. Find console by name")
        print(Fore.YELLOW +"0. Back to main menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            consoles_screen_menu()
        elif choice == "2": 
            find_console_by_name()
        else:
            print(Fore.RED +"Invalid choice, please try again.")

def consoles_screen_menu():
    while True:
        consoles = Console.get_all()

        if not consoles:
            print("No consoles yet. Press N to create one or B to go back")
        else:
            for i, console in enumerate(consoles, start = 1):
                print(f'{i}. {console.name}')


        print(Fore.CYAN + "*** Console List Screen ***")
        print(Fore.YELLOW +"Select a letter from the following options:")
        print(Fore.YELLOW +"A.Add new console U.Update a console B.Back to Consoles Menu")
       
        choice = input("> ").strip().lower()
        if choice == "b":
           break
        elif choice == "a":
            create_console()

        else:
            parts = choice.split()
        
            if parts[0] == "u" and len(parts) > 1:
                try:
                    idx = int(parts[1])
                    selected_console = consoles[idx - 1]
                    print(f"You selected {selected_console.name} to update")
                    update_console(selected_console)
            
                except (ValueError, IndexError):
                    print(Fore.RED + "Invalid number. Try again.")
            elif parts[0] == "b":
                break
            else:
                print(Fore.RED + "Invalid choice, please try again.")


def games_menu():
    while True:
        print(Fore.CYAN + "*** Games Menu ***")
        print(Fore.YELLOW +"1. List all games")
        print(Fore.YELLOW +"2. Find game by name")
        print(Fore.YELLOW +"0. Back to main menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            games_screen_menu()
        elif choice == "2": 
            find_game_by_name()
        else:
            print(Fore.RED +"Invalid choice, please try again.")

def games_screen_menu():
    while True:
        games = Game.get_all()

        if not games:
            print("No games yet. Press A to create one or B to go back")
        else:
            for i, game in enumerate(games, start = 1):
                console = Console.find_by_id(game.console_id)
                console_name = console.name if console else "(Unknown Console)"
                print(f'{i}. {game.title} <{game.genre}> on {console_name}')
    
        print(Fore.CYAN + "*** Game List Screen ***")
        print(Fore.YELLOW +"Select a letter from the following options:")
        print(Fore.YELLOW +"A.Add new game U <#>.Update a game D <#>.Delete a game B.Back to Games Menu")
       
        choice = input("> ").strip().lower()
        if choice == "b":
           break
        elif choice == "a":
            create_game()

        else:
            parts = choice.split()
        
            if parts[0] == "u" and len(parts) > 1:
                try:
                    idx = int(parts[1])
                    selected_game = games[idx - 1]
                    print(f"You selected {selected_game.title} to update")
                    update_game(selected_game)
                except (ValueError, IndexError):
                    print(Fore.RED + "Invalid number. Try again.")

            elif parts[0] == "d" and len(parts) > 1:
                try:
                    idx = int(parts[1])
                    selected_game = games[idx - 1]
                    confirm = input(f"Are you sure you want to delete '{selected_game.title}'? (y/n): ").strip().lower()
                    if confirm == "y":
                        selected_game.delete()
                        print(Fore.GREEN + f"'{selected_game.title}' deleted successfully.")
                    else:
                        print("Deletion canceled.")
                except (ValueError, IndexError):
                    print(Fore.RED + "Invalid number. Try again.")    
                
                
            elif parts[0] == "b":
                break
            else:
                print(Fore.RED + "Invalid choice, please try again.")



if __name__ == "__main__":
    main()




