from . import views
from django.contrib import admin
from django.urls import path
from .views import home, about, contact, blog, blog_single, my_account, destination, sign_up

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('blog/', blog.as_view(), name='blog'),
    path('about/', about.as_view(), name='about'),
    path('contact/', contact.as_view(), name='contact'),
    path('blog_single/', blog_single.as_view(), name='blog_single'),
    path('destination/', destination.as_view(), name='destination'),
    path('my_account/', my_account.as_view(), name='my_account'),
    # path('sign_up/', sign_up.as_view(), name='sign_up'),
    # path('sign_up/', views.sign_up, name='sign_up'),
]
