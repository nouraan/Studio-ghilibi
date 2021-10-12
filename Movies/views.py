from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Films
from . serializer import MyMoviesSerilazier
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from threading import Timer

class MyMoviesList(generics.ListAPIView): 
      queryset = Films.objects.all()
      serializer_class = MyMoviesSerilazier
      filter_backends = [DjangoFilterBackend]
      #The Filter Fields
      filterset_fields   = ['Film','person']
    

      

