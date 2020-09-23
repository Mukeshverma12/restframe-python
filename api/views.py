from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from website.models import Website
from .serializers import Bookserializer


class BookAPIView(generics.ListAPIView):
    queryset = Website.objects.all()
    serializer_class = Bookserializer