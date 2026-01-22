# Simple Library Management System
# Author: Olamide

library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    library.append({"title": title, "author": author})
    print("Book added successfully!\n")

def display_books():
    if not library:
        print("No books in the library.\n")
    else:
        print("\nLibrary Books:")
        for book in library:
            print("Title:", book["title"], "| Author:", book["author"])
        print()

def search_book():
    search_title = input("Enter book title to search: ")
    found = False
    for book in library:
        if book["title"].lower() == search_title.lower():
            print("Book found:", book["title"], "by", book["author"])
            found = True
            break
    if not found:
        print("Book not found.\n")

while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Try again.\n")
