---
from bookshelf.models import Book
### 5.4. Delete  
Delete the book instance and confirm deletion:

```python
book.delete()
books = Book.objects.all()
print(books) 
