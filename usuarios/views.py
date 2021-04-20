from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UsuarioPersCreationForm
from django.urls import reverse_lazy



#vista para crear un usuario personalizado
class RegistrarView(CreateView):
    form_class = UsuarioPersCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registrar.html'
