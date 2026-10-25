"""Project 5: Book Reading List Application
Menu-driven console app to add, view, mark as read, and remove books.
The list is saved to reading_list.json so it is kept between runs.
"""
import json
from pathlib import Path

DATA_FILE = Path("reading_list.json")


def load_books():
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    DATA_FILE.write_text(json.dumps(books, indent=2), encoding="utf-8")


def show_menu():
    print("\n=== Book Reading List ===")
    print("1. Add a book")
    print("2. View reading list")
    print("3. Mark a book as read")
    print("4. Remove a book")
    print("5. Quit")


def view_books(books):
    if not books:
        print("Your reading list is empty.")
        return
    for i, book in enumerate(books, start=1):
        status = "[Read]" if book["read"] else "[To read]"
        print(f"{i}. {book['title']} by {book['author']}  {status}")


def ask_book_index(books):
    """Show the list and return a valid 0-based index, or None."""
    view_books(books)
    if not books:
        return None
    try:
        number = int(input("Enter book number: "))
        if 1 <= number <= len(books):
            return number - 1
    except ValueError:
        pass
    print("Invalid number.")
    return None


def main():
    books = load_books()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            if not title:
                print("Title cannot be empty.")
            else:
                books.append({"title": title, "author": author or "Unknown", "read": False})
                save_books(books)
                print("Added.")
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            i = ask_book_index(books)
            if i is not None:
                books[i]["read"] = True
                save_books(books)
                print("Marked as read.")
        elif choice == "4":
            i = ask_book_index(books)
            if i is not None:
                books.pop(i)
                save_books(books)
                print("Removed.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()