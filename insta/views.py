from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image,Profile,Comment


# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def intro(request):
    date = dt.date.today()
    return render(request, 'all-insta/intro.html', {"date": date,})

def post(request):
    date = dt.date.today()
    images=Image.objects.all()
    comments=Comment.objects.all()
    return render(request, 'all-insta/post.html', {"date": date,"images": images, "comments":comments})

def search_images(request):
  if 'keyword' in request.GET and request.GET["keyword"]:
    search_term = request.GET.get("keyword")
    searched_images = Image.search_images(search_term)
    message = f"{search_term}"

    return render(request, 'all-insta/search.html', {"message":message,"images": searched_images})

  else:
     message = "Not a search term"
     return render(request, 'all-insta/search.html', {"message": message})