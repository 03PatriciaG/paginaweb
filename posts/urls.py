from django.urls import path
from .views import HomePagueView, InformacionPagueView

urlpatterns = [
    path('', HomePagueView.as_view(), name = 'home'),
    path('nota/<int:pk>/', InformacionPagueView.as_view(), name = 'informacion'),
    
]