import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
author_name == (author_name) 
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# List all books in a library
library_name == (library_name)
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()




# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library_name}: {librarian.name}")
