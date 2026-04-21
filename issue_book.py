from utils import books, issued_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books and books[book_name] > 0:
        books[book_name] -= 1
        if book_name in issued_books:
            issued_books[book_name] += 1
        else:
            issued_books[book_name] = 1
        print("Book assigned successfully")
    else:
        print("Book not available")