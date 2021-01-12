from django.shortcuts import render, HttpResponse, redirect
from .models import User, Trip
from django.contrib import messages
import bcrypt

def index(request):
    all_trips = Trip.objects.all()
    context = {
        "all_trips" : all_trips
    }
    return render(request, "index.html", context)

def dashboard(request):
    if 'logged_in_user' not in request.session:
        return redirect('/')
    else:
        context = {
            'logged_in' : User.objects.get(id=request.session['logged_in_user'])
        }
    return render(request, "dashboard.html", context)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['form_password'].encode(), bcrypt.gensalt()).decode()
        newuser = User.objects.create(first_name = request.POST['form_first_name'], last_name = request.POST['form_last_name'], email = request.POST['form_email'], password = hash1)
        request.session['logged_in_user'] = newuser.id
        return redirect('/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['logged_in_user'] = user.id
        return redirect('/dashboard')

def logout(request):
    del request.session['logged_in_user']
    return redirect('/')