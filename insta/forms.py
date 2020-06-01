from django import forms
from .models import Profile,Image,Comment

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
    '''
    class to define profile form
    '''
    class Meta:
        model = Profile
        exlcude = ['user']
        fields = ('bio', 'profile_photo')