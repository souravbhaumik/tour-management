from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("sign_up")
            else:
                user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User created successfully")
        else:
            messages.info(request, "Both passwords are not matched")
            return redirect("sign_up")
        return redirect("/")
    else:
        return render(request, "sign_up.html")