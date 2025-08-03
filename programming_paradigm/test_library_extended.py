from library_management import Book, Library

def test_extended_functionality():
    print("=== Extended Library Management Test ===\n")
    
    # Setup library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    
    print("1. Initial setup:")
    library.list_available_books()
    
    print("\n2. Check out '1984':")
    success = library.check_out_book("1984")
    print(f"Checkout successful: {success}")
    library.list_available_books()
    
    print("\n3. Try to check out '1984' again (should fail):")
    success = library.check_out_book("1984")
    print(f"Checkout successful: {success}")
    library.list_available_books()
    
    print("\n4. Try to return 'Brave New World' (not checked out):")
    success = library.return_book("Brave New World")
    print(f"Return successful: {success}")
    library.list_available_books()
    
    print("\n5. Return '1984':")
    success = library.return_book("1984")
    print(f"Return successful: {success}")
    library.list_available_books()
    
    print("\n6. Check out non-existent book:")
    success = library.check_out_book("Non-existent Book")
    print(f"Checkout successful: {success}")
    library.list_available_books()

if __name__ == "__main__":
    test_extended_functionality() 