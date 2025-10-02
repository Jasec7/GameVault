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
        print("*** Main Menu ***")
        print("1. Consoles")
        print("2. Games")
        print("0. Exit")

        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            consoles_menu()
        elif choice == "2":
            games_menu()
        else: 
             print("Invalid choice, please try again.")



def consoles_menu():
    while True:
        print("*** Consoles Menu ***")
        print("1. List all consoles")
        print("2. Find console by name")
        print("3. Find console by id")
        print("4. Create console")
        print("5. Update console")
        print("6. Delete console")
        print("0. Back to main menu")

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
            print("Invalid choice, please try again.")

def games_menu():
    while True:
        print("*** Games Menu ***")
        print("1. List all games")
        print("2. Find game by name")
        print("3. Find game by id")
        print("4. Create game")
        print("5. Update game")
        print("6. Delete game")
        print("0. Back to main menu")

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
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
