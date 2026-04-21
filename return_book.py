from utils import issued_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issued_books and issued_books[book_name] > 0:
        issued_books[book_name] -= 1
        if book_name in books:
            books[book_name] += 1
        else:
            books[book_name] = 1
        print("Book returned")
    else:
        print("Book not issued or does not exist")