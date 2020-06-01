from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image,Profile,Comment
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def intro(request):
    date = dt.date.today()
    return render(request, 'all-insta/intro.html', {"date": date,})

@login_required(login_url='/accounts/login/')
def post(request):
    date = dt.date.today()
    images=Image.objects.all()
    comments=Comment.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('post')
    else:
        form = NewsLetterForm()
    return render(request, 'all-insta/post.html', {"date": date,"images": images, "comments":comments,"letterForm":form})

@login_required(login_url='/accounts/login/')
def search_images(request):
  if 'keyword' in request.GET and request.GET["keyword"]:
    search_term = request.GET.get("keyword")
    searched_images = Image.search_images(search_term)
    message = f"{search_term}"

    return render(request, 'all-insta/search.html', {"message":message,"images": searched_images})

  else:
     message = "Not a search term"
     return render(request, 'all-insta/search.html', {"message": message})

@login_required(login_url='/accounts/login/')  
def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'profile/create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')  
def profile(request,id): 
    try: 
        current_user = request.user
        profile = Profile.objects.filter(user_id=id).all()
        images = Image.objects.filter(profile_id=current_user.profile.id).all()
        return render(request, 'profile/profile.html', {"profile":profile, "images":images}) 
    except User.profile.RelatedObjectDoesNotExist:
        current_user = request.user
        if request.method=="POST":
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile =form.save(commit=False)
                profile.user = current_user
                profile.save()
                return render(request, 'profile/profile.html', {"profile":profile, "images":images}) 
        else:
            form = ProfileForm()
        return render(request, 'profile/create_profile.html',{"form":form})
