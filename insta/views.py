from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def intro(request):
    date = dt.date.today()
    return render(request, 'all-insta/intro.html', {"date": date,})

def post(request):
    date = dt.date.today()
    return render(request, 'all-insta/post.html', {"date": date,})