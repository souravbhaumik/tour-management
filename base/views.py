from django.http import JsonResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

class home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class about(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

class contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')

class blog_single(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog_single.html')

class blog(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog.html')

class destination(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'destination.html')

class my_account(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign_in.html')

# class sign_up(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'sign_up.html')
    
def sign_up(request):
    if request.method == 'POST':
        Name = request.POST["full_name"]
        Email = request.POST["email"]
        Password = request.POST["password"]
        Confirm_password = request.POST["confirm_password"]

        user = User.objects.create_user(username = Email, email=Email, password=Password, name=Name)
        user.save()
        return redirect("/")

    else:
        return render(request, "sign_up.html")