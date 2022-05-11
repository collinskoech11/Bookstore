from django.db import models
# Create your models here.

class Author(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Date_of_birth = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField(default=2012)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
