from django.db import models
from django.db.models import fields
from rest_framework import serializers
from Movies.models import Films


from celery import Celery
from celery.schedules import crontab



class MyMoviesSerilazier(serializers.ModelSerializer):
    #The Related Field
    person = serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Films
        fields = ['Film','person']


        # fields='__all__'
       
   