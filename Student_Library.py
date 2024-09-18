'''Project 3 - Student Library
Implement a student library system using OOPs where sdtudents can orrow a book from the list of books.
Create a separate library and student class.
Your program must be menu driven
You are fee to choose methods and attributes
of your choice to implement this program

'''

class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, quantity):
        """Add a book to the library with the given quantity."""
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"Added {quantity} copies of '{title}' to the library.")

    def list_books(self):
        """List all books in the library with their quantities."""
        print("Books available in the library:")
        for title, quantity in self.books.items():
            print(f"- {title}: {quantity} copies")

    def borrow_book(self, title, student_name):
        """Allow a student to borrow a book if available."""
        if title in self.books and self.books[title] > 0:
            if title not in self.borrowed_books:
                self.borrowed_books[title] = []
            self.borrowed_books[title].append(student_name)
            self.books[title] -= 1
            print(f"'{title}' has been borrowed by {student_name}.")
        else:
            print(f"Sorry, '{title}' is not available.")

    def return_book(self, title, student_name):
        """Allow a student to return a borrowed book."""
        if title in self.borrowed_books and student_name in self.borrowed_books[title]:
            self.borrowed_books[title].remove(student_name)
            self.books[title] += 1
            print(f"'{title}' has been returned by {student_name}.")
        else:
            print(f"Sorry, {student_name} did not borrow '{title}'.")

class Student:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, library, title):
        """Student borrows a book from the library."""
        library.borrow_book(title, self.name)

    def return_book(self, library, title):
        """Student returns a book to the library."""
        library.return_book(title, self.name)

def menu():
    """Display the menu and handle user choices."""
    library = Library()
    students = {}

    while True:
        print("\nLibrary System Menu:")
        print("1. Add a book")
        print("2. List all books")
        print("3. Register a student")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                title = input("Enter the book title: ")
                quantity = int(input("Enter the quantity: "))
                library.add_book(title, quantity)
            case "2":
                library.list_books()
            case "3":
                name = input("Enter the student's name: ")
                if name not in students:
                    students[name] = Student(name)
                    print(f"Student {name} registered.")
                else:
                    print(f"Student {name} is already registered.")
            case "4":
                name = input("Enter the student's name: ")
                title = input("Enter the book title: ")
                if name in students:
                    students[name].borrow_book(library, title)
                else:
                    print(f"Student {name} is not registered.")
            case "5":
                name = input("Enter the student's name: ")
                title = input("Enter the book title: ")
                if name in students:
                    students[name].return_book(library, title)
                else:
                    print(f"Student {name} is not registered.")
            case "6":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    menu()
