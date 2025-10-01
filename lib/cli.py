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
        menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
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
        elif choice == "7":
            list_games()
        elif choice == "8":
            find_game_by_name()
        elif choice == "9":
            find_game_by_id()
        elif choice == "10":
            create_game()
        elif choice == "11":
            update_game()
        elif choice == "12":
            delete_game()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all consoles")
    print("2. Find console by name")
    print("3. Find consolet by id")
    print("4. Create console")
    print("5. Update console")
    print("6. Delete console")
    print("7. List all games")
    print("8. Find game by name")
    print("9. Find game by id")
    print("10. Create game")
    print("11. Update game")
    print("12. Delete game")


if __name__ == "__main__":
    main()
