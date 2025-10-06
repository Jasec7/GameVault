# 🕹️Game VAULT.
It's a command line application where you can manage you video game collection by consoles and genres.

## Overview
GameVault is a Python-based CLI app that allows users to manage their collection of video games and consoles.
Users can add, update, view, or delete consoles and games, and easily view games for a specific console — all through a clean, color-coded interface.

## Features
- Add, update, list, and delete consoles 🎮
- Add, update, list, and delete games 🕹️
- View all games belonging to a specific console
- Input validation with informative error messages
- Database constraints and ON DELETE CASCADE for data integrity
- Clean CLI menus for presentative navigation

## Technologies Used
- Python 3
- SQLite3 (with foreign key support)
- Colorama (for colored CLI output)


## Getting Started
1. Clone the repository
```
git clone https://github.com/your-username/gamevault.git
cd gamevault
```
2. Install dependencies 
```
pipenv install
pipenv shell
```
3. Run the program
```
python lib/cli.py
```

## Data Model
Console:
- id (Primary Key)
- name (Unique, Not Null)

Game:
- id (Primary Key)
- title (Not Null)
- genre (Not Null)
- console_id (Foreign Key → Console.id, ON DELETE CASCADE)

Relationship:
- One Console → Many Games

## CLI Navigation
```
 Main Menu

C. Consoles
G. Games
E. Exit

Consoles Menu

List consoles
Find console by name
A. Add a console -- U <#>. Update a console -- D. <#> Delete a consoles -- V <#>. View games -- B.Back to menu

 Games Menu

List games
Find game by name
A. Add a console -- U <#>. Update a console -- D. <#> Delete a consoles -- V <#>. View games -- B.Back to menu
```
## Example Interaction
```
Welcome to GameVault!

*** Main Menu ***

C. Consoles
G. Games
E. Exit
> c

*** Consoles Menu ***

1. List all consoles
2. Find console by name
0. Back to main menu
> 1

*** Console List Screen ***
1. PS5
2. Nintendo Switch

A. Add a console  U <#>. Update a console  D <#>. Delete a console  V <#>. View games  B. Back to menu
```

## 📝 License
This project is licensed under the MIT License.

## Contributors
- [Jasec7](https://github.com/Jasec7)



