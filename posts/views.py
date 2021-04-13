from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Post
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy




#aqui se crean las vistas para nuestra pagina

class HomePagueView(TemplateView):
    model = Post #utilizando el modelo Post en donde se encuentra la llave y la infromacion principal
    template_name = 'home.html' #se va a dirigir al html llaamado home
    context_object_name = 'blogs' #utilizaremos un objeto llamado blogs en donde vendra la informacion de posts


class InformacionPagueView(DetailView):
    model = Post    #utilizando el modelo Post en donde se encuentra la llave y la infromacion principal
    template_name = 'cortes.html' #se va a dirigir al html llaamado cortes
    context_object_name = 'blogs'#utilizaremos un objeto llamado blogs en donde vendra la informacion de posts

class notaCreateView(CreateView):
    model = Post  #utilizando el modelo Post en donde se encuentra la llave y la infromacion principal
    template_name = 'notaNueva.html'  #se va a dirigir al html llaamado notaNueva
    fields = '__all__'  #nos permitira crear todos los cambios de posts

class notaUpdateView(UpdateView):
    model = Post  #utilizando el modelo Post en donde se encuentra la llave y la infromacion principal
    template_name = 'editarDetalle.html'  #se va a dirigir al html llaamado editarDetalle
    fields =[ 'titulo', 'informacion'] #aqui se podran actualizar los datos de una nota menos el precio(en mi caso)
    
class notaDeleteView(DeleteView):
    model = Post  #utilizando el modelo Post en donde se encuentra la llave y la infromacion principal
    template_name = 'eliminarDetalle.html'  #se va a dirigir al html llaamado eliminarDetalle
    context_object_name = 'blogs'
    success_url = reverse_lazy('home') #al eliminar la nota nos regresara a la pagina principal
    
class VideoView(ListView):
    model = Post  #utilizando el modelo Post en donde se encuentra la llave y la infromacion principal
    template_name = 'video.html'  #se va a dirigir al html llaamado eliminarDetalle
    context_object_name = 'blogs' #utilizaremos un objeto llamado blogs en donde vendra la informacion de posts
    
