from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    if "login_id" not in request.session:
        return redirect ('/')
    context = {
        'trips': My_Trip.objects.filter(trip_user=request.session['login_id']),
        'other_trips': My_Trip.objects.exclude(trip_user=request.session['login_id'])
    }
    return render(request, 'travel/index.html', context)

def add(request):
    if "login_id" not in request.session:
        return redirect ('/')
    return render(request, 'travel/add.html')

def create(request):
    if "login_id" not in request.session:
        return redirect ('/')
    errors = My_Trip.objects.validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/travels/add')
    if request.method == 'POST':
        trip = My_Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], travel_start=request.POST['travel_from'], travel_end=request.POST['travel_to'], created_user= User.objects.get(id=request.session['login_id']))
        trip.trip_user.add(User.objects.get(id=request.session['login_id']))
    return redirect('/travels')

def view(request, id):
    if "login_id" not in request.session:
        return redirect ('/')
    trip = My_Trip.objects.get(id=id)
    context = {
        'trips': My_Trip.objects.filter(id=id),
        'other_trips': User.objects.filter(join_trip=id).exclude(id=trip.created_user.id)
    }
    return render(request, 'travel/view.html', context)


def destroy(request, id):
    if "login_id" not in request.session:
        return redirect ('/')
    trip = My_Trip.objects.get(id=id)
    trip.delete()
    return redirect('/travels')

def cancel(request, id):
    if "login_id" not in request.session:
        return redirect ('/')
    trip = My_Trip.objects.get(id=id)
    trip.trip_user.remove(User.objects.get(id=request.session['login_id']))
    return redirect('/travels')

def join(request, id):
    if "login_id" not in request.session:
        return redirect ('/')
    trip = My_Trip.objects.get(id=id)
    trip.trip_user.add(User.objects.get(id=request.session['login_id']))
    return redirect ('/travels')
