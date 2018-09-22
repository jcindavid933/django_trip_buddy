from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'login_register/index.html')

def success(request):
    if "login_id" not in request.session:
        return redirect ('/')
    return render(request, 'travel/index.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    elif request.method == 'POST':
        hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashpw.decode())
        request.session['login_id'] = user.id
        request.session['name'] = user.first_name
        request.session['count'] = 0
    return redirect('/travels/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    elif request.method == 'POST':
        user = User.objects.filter(email=request.POST['login_email'])
        request.session['login_id'] = user[0].id
        request.session['name'] = user[0].first_name
        request.session['count'] = 1
    return redirect('/travels/')

def reset(request):
    request.session.clear()
    return redirect('/')
