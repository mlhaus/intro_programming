#!/usr/bin/env python3

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()

def list(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")
    print()

def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")

def delete(movie_list):
    list(movie_list)
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")

def press_enter_to_continue():
    input("\nPress enter to continue...")

def main():
    movie_list = ["Monty Python and the Holy Grail",
                  "On the Waterfront",
                  "Cat on a Hot Tin Roof"]

    while True:
        display_menu()
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)   
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)  
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
        press_enter_to_continue()

    print("Bye!")

if __name__ == "__main__":
    main()
