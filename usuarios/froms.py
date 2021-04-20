from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPers


#Formulario para poder crear un usuario personalizado
class UsuarioPersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPers
        fields = UserCreationForm.Meta.fields + ('email','edad', 'telefono')

#formulario para cambiar el usuario personalizado
class UsuarioPersChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioPers
        fields = UserChangeForm.Meta.fields
