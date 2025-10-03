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
        print(Fore.YELLOW +"1. Consoles")
        print(Fore.YELLOW +"2. Games")
        print(Fore.YELLOW +"0. Exit")

        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            consoles_menu()
        elif choice == "2":
            games_menu()
        else: 
             print(Fore.RED +"Invalid choice, please try again.")



def consoles_menu():

    while True:
        print(Fore.CYAN + "*** Consoles Menu ***")
        print(Fore.YELLOW +"1. List all consoles")
        print(Fore.YELLOW +"2. Find console by name")
        print(Fore.YELLOW +"3. Create console")
        print(Fore.YELLOW +"4. Update console")
        print(Fore.YELLOW +"5. Delete console")
        print(Fore.YELLOW +"0. Back to main menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            consoles_screen_menu()
        elif choice == "2": 
            find_console_by_name()
        elif choice == "3": 
            create_console()
        elif choice == "4": 
            update_console()
        elif choice == "5": 
            delete_console()
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
        print(Fore.YELLOW +"N. Add new console U <#> Update a console B. Back to Consoles Menu")
       
        choice = input("> ").strip().lower()
        if choice == "b":
           break
        elif choice == "n":
            create_console()
            
        else:
            parts = choice.split()
        
            if parts[0] == "u" and len(parts) > 1:
                try:
                    idx = int(parts[1])
                    selected_console = consoles[idx - 1]
                    print(f"You selected {selected_console.name} to update")
            
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
        print(Fore.YELLOW +"3. Create game")
        print(Fore.YELLOW +"4. Update game")
        print(Fore.YELLOW +"5. Delete game")
        print(Fore.YELLOW +"0. Back to main menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            list_games()
        elif choice == "2": 
            find_game_by_name()
        elif choice == "3": 
            create_game()
        elif choice == "4": 
            update_game()
        elif choice == "5": 
            delete_game()
        else:
            print(Fore.RED +"Invalid choice, please try again.")

if __name__ == "__main__":
    main()




