from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy




# Create your views here.

class HomePagueView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blogs'

class InformacionPagueView(DetailView):
    model = Post
    template_name = 'cortes.html'
    context_object_name = 'blogs'

class notaCreateView(CreateView):
    model = Post
    template_name = 'notaNueva.html'
    fields = '__all__' 

class notaUpdateView(UpdateView):
    model = Post
    template_name = 'editarDetalle.html'
    fields =[ 'text', 'informacion']
    
class notaUpdateView(DeleteView):
    model = Post
    template_name = 'eliminarDetalle.html'
    context_object_name = 'Blogs'
    success_url = reverse_lazy('home')
    