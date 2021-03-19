from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post





# Create your views here.

class HomePagueView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blogs'

class InformacionPagueView(DetailView):
    model = Post
    template_name = 'cortes.html'
    context_object_name = 'blogs'




    
    