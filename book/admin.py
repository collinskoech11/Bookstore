from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','year')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fname','email')

# admin.site.register(Links, LinksAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)