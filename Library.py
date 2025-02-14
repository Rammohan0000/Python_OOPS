class Book:
    def __init__(self, name, genre, published_date, rating):
        print(f"Creating book: {name}, Genre: {genre}, Published Date: {published_date}, Rating: {rating}")
        self.name = name
        self.genre = genre
        self.published_date = published_date
        self.rating = rating

class Library:
    def __init__(self):
        print("Initializing library...")
        self.books = []
    
    def add_book(self, book):
        print(f"Adding book: {book.name}")
        self.books.append(book)
    
    def get_best_rated_book(self, genre):
        print(f"Searching for best-rated book in genre: {genre}")
        genre_books = [book for book in self.books if book.genre.lower() == genre.lower()]
        if not genre_books:
            print("No books found in this genre.")
            return "No books found in this genre."
        best_book = max(genre_books, key=lambda x: x.rating)
        print(f"Best rated book found: {best_book.name} with rating {best_book.rating}")
        return f"Best Rated Book in {genre} Genre:\nName: {best_book.name}\nPublished Date: {best_book.published_date}\nRating: {best_book.rating}"

# Main Execution
print("Starting Library Management System...")
library = Library()

num_books = int(input("Enter number of books: "))
print(f"Number of books to add: {num_books}")
for _ in range(num_books):
    name = input("Enter book name: ")
    genre = input("Enter genre: ")
    published_date = input("Enter published date (YYYY-MM-DD): ")
    rating = float(input("Enter rating (out of 5): "))
    
    book = Book(name, genre, published_date, rating)
    library.add_book(book)

search_genre = input("Enter the genre to find the best-rated book: ")
print(library.get_best_rated_book(search_genre))
