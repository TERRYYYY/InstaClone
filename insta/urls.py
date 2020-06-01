from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.intro,name='intro'),
    url('^post/$',views.post,name='post'),
    url(r'^new/post$',views.new_post,name="new_post"),
    url(r'^search/', views.search_images, name='search_images'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^accounts/profile',views.profile,name='profile'),
    url(r'^createprofile',views.create_profile,name="create_profile"),
    # url('^$',views.intro,name = 'intro'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)