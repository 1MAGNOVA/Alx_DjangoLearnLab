from .models import Book
from django.contrib import admin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
   list_filter = ("title" ,"author", "publication_year")
   search_fields = ("title", "author" , "publication_year")


admin.site.register(Book, BookAdmin)
