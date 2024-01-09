from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    return render(request, "home.html")

def signin(request):
    return render(request, 'signin.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pas1 = request.POST['pas1']
        pas2 = request.POST["pas2"]

        myuser = User.objects.create(username, email, pas1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect("signin")
    return render(request, "signup.html")
def signout(request):
    return render(request, "signout.html")