from django.test import TestCase
from .models import Image,Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        self.image= Image(image_name = 'Beagle', caption ='Lovely dog',pub_date ='2020-06-01', likes='20', image_file ='images/beagle.jpg')
        self.image.save_image()

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()

class ProfileTestClass(TestCase):
    '''
    test class to test methods of the profile class
    '''
    def setUp(self):
        self.profile=Profile(user="victor",profile_pic="pic",bio="person")

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    
