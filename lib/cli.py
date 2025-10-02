from colorama import Fore, Style, init
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
        print(Fore.YELLOW +"3. Find console by id")
        print(Fore.YELLOW +"4. Create console")
        print(Fore.YELLOW +"5. Update console")
        print(Fore.YELLOW +"6. Delete console")
        print(Fore.YELLOW +"0. Back to main menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            list_consoles()
        elif choice == "2": 
            find_console_by_name()
        elif choice == "3": 
            find_console_by_id()
        elif choice == "4": 
            create_console()
        elif choice == "5": 
            update_console()
        elif choice == "6": 
            delete_console()
        else:
            print(Fore.RED +"Invalid choice, please try again.")

def games_menu():
    while True:
        print(Fore.CYAN + "*** Games Menu ***")
        print(Fore.YELLOW +"1. List all games")
        print(Fore.YELLOW +"2. Find game by name")
        print(Fore.YELLOW +"3. Find game by id")
        print(Fore.YELLOW +"4. Create game")
        print(Fore.YELLOW +"5. Update game")
        print(Fore.YELLOW +"6. Delete game")
        print(Fore.YELLOW +"0. Back to main menu")

        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            list_games()
        elif choice == "2": 
            find_game_by_name()
        elif choice == "3": 
            find_game_by_id()
        elif choice == "4": 
            create_game()
        elif choice == "5": 
            update_game()
        elif choice == "6": 
            delete_game()
        else:
            print(Fore.RED +"Invalid choice, please try again.")

if __name__ == "__main__":
    main()
