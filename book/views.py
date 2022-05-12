from django.shortcuts import render
from book.models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#Book serializers
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class AuthorBookList(APIView):
     def get(self, request,pk):
        books = Book.objects.filter(Author=pk)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class YearBookList(APIView):
    def get(self, request,pk):
        books = Book.objects.filter(year=pk)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookEdit(APIView):
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     book = self.get_object(pk)
    #     book.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



#Author serializers
class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

class AuthorCreate(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

class AuthorEdit(APIView):
    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     author = self.get_object(pk)
    #     author.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

