# Library Book Record System

library = {
    "B101": {"title": "Python Programming", "author": "John Smith", "price": 450},
    "B102": {"title": "Machine Learning", "author": "Andrew Ng", "price": 550},
    "B103": {"title": "Cloud Computing", "author": "Raj Kumar", "price": 600}
}

while True:
    print("\n--- Library Book Record System ---")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nBook Records:")
        for book_id, details in library.items():
            print("Book ID:", book_id)
            print("Title:", details["title"])
            print("Author:", details["author"])
            print("Price:", details["price"])
            print()

    elif choice == "2":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        price = float(input("Enter Book Price: "))

        library[book_id] = {
            "title": title,
            "author": author,
            "price": price
        }

        print("Book added successfully!")

    elif choice == "3":
        book_id = input("Enter Book ID to update: ")

        if book_id in library:
            library[book_id]["title"] = input("Enter new title: ")
            library[book_id]["author"] = input("Enter new author: ")
            library[book_id]["price"] = float(input("Enter new price: "))

            print("Book updated successfully!")
        else:
            print("Book ID not found.")

    elif choice == "4":
        book_id = input("Enter Book ID to delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully!")
        else:
            print("Book ID not found.")

    elif choice == "5":
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            print("Book Found!")
            print("Title:", library[book_id]["title"])
            print("Author:", library[book_id]["author"])
            print("Price:", library[book_id]["price"])
        else:
            print("Book not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice")