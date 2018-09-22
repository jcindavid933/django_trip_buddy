from __future__ import unicode_literals
from django.db import models
from apps.login_register.models import User
from datetime import datetime
from time import strftime

class TripManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['description']) < 1:
            errors['description'] = 'Please enter a description'
        if len(postData['destination']) < 1:
            errors['destination'] = 'Please enter a destination'
        if not postData['travel_from']:
            errors['travel_from'] = 'Please enter a travel from date'
        if not postData['travel_to']:
            errors['travel_to'] = 'Please enter a travel to date'
        if postData['travel_from'] > postData['travel_to']:
            errors['travel_to'] = 'Please enter a departure date that is before the arrival date!'
        d = datetime.now()
        now = d.strftime('%Y-%m-%d')
        if postData['travel_from'] < now:
            errors['travel_before'] = 'Please enter a date that aint in the past'
        return errors

class My_Trip(models.Model):
    destination = models.CharField(max_length=255)
    travel_start = models.DateField()
    travel_end = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_user = models.ForeignKey(User, related_name='user_trip', on_delete = models.CASCADE)
    trip_user = models.ManyToManyField(User, related_name='join_trip')

    objects = TripManager()
