looking_book = input()

is_book_found = False
books_count = 0
input_line = input()
while input_line != "No More Books":
    if input_line == looking_book:
        is_book_found = True
        break

    books_count += 1

    input_line = input()

if is_book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")