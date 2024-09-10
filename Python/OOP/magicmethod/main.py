# Magic methods = Dunder methods (double underscore) __Init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developer to define or customize the behavior of objects


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title  # Initialize the title attribute
        self.author = author  # Initialize the author attribute
        self.num_pages = num_pages  # Initialize the num_pages attribute

    def __str__(self):
        # Return a string representation of the book
        return f"{self.title} By {self.author}"

    def __eq__(self, other):
        # Check if two books are equal based on title and author
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        # Check if this book has fewer pages than another book
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        # Check if this book has more pages than another book
        return self.num_pages > other.num_pages

    def __add__(self, other):
        # Add the number of pages of two books
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        # Check if a keyword is in the title or author of the book
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        # Get the value of an attribute based on the key
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"

# Create instances of Book with different titles, authors, and number of pages
book1 = Book("The habiit", "J.J.R Tokien", 310)
book2 = Book("Harry Potter", "J.K Rowling ", 233)
book3 = Book("The Lion, The witch and the wardrobe", "C.S Lewis", 172)
book4 = Book("The habiit", "J.J.R Tokien", 310)

# Print the string representation of book1
print(book1)

# Check if book1 is equal to book4 and print the result
print(book1 == book4)
# Check if book2 has fewer pages than book3 and print the result
print(book2 < book3)
# Check if book2 has more pages than book3 and print the result
print(book2 > book3)
# Add the number of pages of book1 and book2 and print the result
print(book1 + book2)

# Check if the keyword "Habiit" is in the title or author of book1 and print the result
print("Habiit" in book1)
# Check if the keyword "Lion" is in the title or author of book2 and print the result
print("Lion" in book2)
# Check if the keyword "Lion" is in the title or author of book3 and print the result
print("Lion" in book3)

# Get and print the title of book3
print(book3['title'])
# Get and print the author of book3
print(book3['author'])
# Get and print the number of pages of book3
print(book3['num_pages'])
# Try to get a non-existent key "Audio" from book3 and print the result
print(book3['Audio'])
