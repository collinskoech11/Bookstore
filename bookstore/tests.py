from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from book.models import Book, Author
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # below code will fix AttributeError: type object 'Model Test' has no attribute 'cls_atomics' error.
        super(ModelTest, cls).setUpClass()
        # test Book Model
        # create a Author model object in temporary database.
        sampleauthor = Author(fname='tom', lname='onyango', email="tom@gmail.com", Date_of_birth='2000-12-12')
        sampleauthor.save()
        # get author .
        sampleuthor = Author.objects.get(fname='tom')
        print('Added author data : ', sampleauthor)
        # create and save the Author object.
    def testAuthorModel(self):
        sampleauthor = Author.objects.get(lname='onyango')
        self.assertEqual(sampleauthor.fname,'tom')
        print(sampleauthor)
        return sampleauthor

# class TestAuthorCreate(APITestCase):
#     def can_create_author(self):
#         sample_author = {
#             'fname':'sample',
#             'lname':'author',
#             'email':'sample@gmail.com',
#             'Date_of_birth':'2000-12-12',
#         }
#         response = self.client.post(reverse('authors/new'), sample_author )
#         self.AssertEqual(response.status_code, status.HTTP_200_OK)
#         pass
        # factory = APIRequestFactory()
        # request = factory.get('books')
        # request.book = book
        # response = view(request)
        
        # request = factory.post('authors/new',{'fname':'sample', 'sname':'lastname','email':'sample@gmail.com','Date_of_birth':'2000-12-12'}, format='json')
#         data = {
#             'fname':'samuel',
#             'sname':'wanjiru',
#             'email':'samuel@gmail.com',
#             'Date_of_birth':'10-09-2000',   
#         }
#         response = self.client.post('authors/new', data=data)
#         self.assertContains(response,"fname")
#         # self.assertContains(response,"sname")
#         # self.assertContains(response,"email")
#         # self.assertContains(response,"Date_of_birth")
