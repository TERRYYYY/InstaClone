from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=255)
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    image_file = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']
    
    def save_image(self):
        self.save()

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')
    bio = models.TextField(default = '')
    user = models.OneToOneField(User, on_delete = models.CASCADE, default='')

    def __str__(self):
        return self.bio
    class Meta:
        ordering = ['bio']

    # def save_profile(self):
    # self.save()
class Comment(models.Model):

    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_file = models.ForeignKey(Image, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    class Meta:
        ordering = ['comment']
