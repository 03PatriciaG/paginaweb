from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioPersCreationForm, UsuarioPersChangeForm
from .models import UsuarioPers


class UsuarioPersAdmin(UserAdmin):
    add_form = UsuarioPersCreationForm
    form = UsuarioPersChangeForm
    model = UsuarioPers
    list_display = ['username', 'edad', 'telefono', 'is_staff', ]

#registramos UsuarioPers y UsuarioPersAdmin
admin.site.register(UsuarioPers, UsuarioPersAdmin)
