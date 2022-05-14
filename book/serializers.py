from re import I
from .models import *
from rest_framework import serializers
status = "bad"

class BookSerializer(serializers.ModelSerializer):
    book_status = serializers.SerializerMethodField('_get_book_status')

    def _get_book_status(self, book_object):
        global status
        quantity = getattr(book_object, 'quantity')
        if quantity > 10:
            status = "good"
            return status
        elif quantity > 4 and quantity < 10:
            status = "Bad"
            return status
        elif quantity > 0 and quantity < 5:
            status = "Critical"
            return status
        elif quantity == 0:
            status = "Out of stock"
            return status
    class Meta:
        model = Book
        fields = ['id','title','Author','year','description','quantity','book_status']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','fname','lname','email','Date_of_birth']