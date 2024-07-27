class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
        # Removed the print statement for expected output

    def __del__(self):
        """Destructor that prints a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


