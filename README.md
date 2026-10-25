# book-reading-list-application
# Project 5: Book Reading List Application (Python)

A menu-driven console app to manage a personal reading list.

## Description
Add books with a title and author, view the list, mark books as read, and remove books you no longer want. Each book shows a `[Read]` or `[To read]` status.

## Technologies
- Puthon17
- Standard library: `iostream`, `vector`, `string`, `limits`

## Features
- Add a book (title and author)
- View the full reading list with status
- Mark a book as read
- Remove a book
- Input validation for menu choices and book numbers
- Handles an empty list without errors

## Setup and Run
```
g++ -std=c++17 project5_book_reading_list.cpp -o readinglist
./readinglist
```

## Example
```
=== Book Reading List ===
1. Add a book
2. View reading list
3. Mark a book as read
4. Remove a book
5. Quit
Choose an option: 2
1. Clean Code by Robert Martin  [Read]
```

## Limitations
- The list is kept in memory only, so it is lost when the program closes.
- Possible future improvement: save and load the list from a text file.

## Notes
This is a console version. The Lecture 11 reading list was a deployed web app, so this C++ project is separate and has no live link.
