from django.test import TestCase
# from .models import Image,Profile,Comment
# from django.contrib.auth.models import User

# # Create your tests here.
# class ImageTestCase(TestCase):
#     def setUp(self):
#         self.image= Image(image_name = 'Beagle', caption ='Lovely dog',pub_date ='2020-06-01', likes='20', image_file ='images/beagle.jpg')
#         self.image.save_image()

#     def test_save_images(self):
#         self.image.save_image()
#         all_images = Image.objects.all()
#         self.assertTrue(len(all_images) > 0)