class Book:
    def __init__(self, name, genre, published_date, rating):
        self.name = name
        self.genre = genre.lower()  
        self.published_date = published_date
        self.rating = rating

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_best_rated_book(self, genre):
        genre_books = [book for book in self.books if book.genre == genre.lower()]
        if not genre_books:
            return "No books found in this genre."
        best_book = max(genre_books, key=lambda x: x.rating)
        return f"Best Rated Book in {genre}:\nName: {best_book.name}\nPublished Date: {best_book.published_date}\nRating: {best_book.rating}"

# Main Execution
library = Library()
num_books = int(input("Enter number of books: "))

for _ in range(num_books):
    book = Book(
        input("Enter book name: "),
        input("Enter genre: "),
        input("Enter published date (YYYY-MM-DD): "),
        float(input("Enter rating (out of 5): "))
    )
    library.add_book(book)

search_genre = input("Enter genre to find the best-rated book: ")
print(library.get_best_rated_book(search_genre))
