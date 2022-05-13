from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.


class modelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ModelTest, cls).setUpClass()

        booksample = Book(title='The World of geography', Author=1, year=2013, description='sample', quantity='2')
        booksample.save()
        print(booksample)