from django.test import TestCase
from django.contrib.auth.models import User
from book.models import Book, Author
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