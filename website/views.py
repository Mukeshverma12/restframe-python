from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Website

class BookListView(ListView):
    model = Website
    template_name = 'website/book.html'
