from utils import books

def show():
    if len(books) == 0:
        print("Book not available")
    else:
        for book_name in books:
            print(f"{book_name} - Copies: {books[book_name]}")