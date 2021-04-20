from django.urls import path
from .views import RegistrarView

urlpatterns = [
    path('', RegistrarView.as_view(), name="registrar"),

]
