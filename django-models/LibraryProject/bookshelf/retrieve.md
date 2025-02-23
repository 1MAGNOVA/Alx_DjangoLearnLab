---

### 5.2. Retrieve  
Retrieve and display all attributes of the created book:

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year) 
