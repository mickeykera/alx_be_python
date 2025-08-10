class Book:
    """Base class for all types of books"""
    
    def __init__(self, title: str, author: str):
        """Initialize book attributes"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class EBook(Book):
    """EBook class inheriting from Book"""
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize EBook attributes"""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation of the EBook"""
        return f"{super().__str__()} (EBook, {self.file_size} KB)"


class PrintBook(Book):
    """PrintBook class inheriting from Book"""
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize PrintBook attributes"""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of the PrintBook"""
        return f"{super().__str__()} (Print Book, {self.page_count} pages)"


class Library:
    """Library class demonstrating composition by managing a collection of books"""
    
    def __init__(self):
        """Initialize library with empty book collection"""
        self.books = []
    
    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library"""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Error: Can only add Book instances to the library")
    
    def list_books(self):
        """Print details of each book in the library"""
        if not self.books:
            print("The library is empty.")
            return
        
        print("\n=== Library Catalog ===")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("=======================")
