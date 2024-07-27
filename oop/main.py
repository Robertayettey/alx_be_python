from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create different instances of books
    classic_book = Book("To Kill a Mockingbird", "Harper Lee")
    digital_novel = EBook("Dune", "Frank Herbert", 600)
    paper_novel = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    print("Books in the library:")
    my_library.list_books()

    # Additional tests or functionality can be added here

if __name__ == "__main__":
    main()


