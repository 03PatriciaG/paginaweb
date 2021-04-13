from django.urls import path
from .views import HomePagueView, InformacionPagueView, notaCreateView, notaUpdateView, notaDeleteView
from .views import VideoView
urlpatterns = [

    #path para diriginirnos a cada una de nuestros templates usando la llave primaria
    
    path('video', VideoView.as_view(), name = 'video'),
    path('nota/<int:pk>/eliminar', notaDeleteView.as_view(), name="eliminarDetalle"),
    path('nota/<int:pk>/editar', notaUpdateView.as_view(), name="editarDetalle"),
    path('nota/Nueva', notaCreateView.as_view(), name='notaNueva'),
    path('nota/<int:pk>/', InformacionPagueView.as_view(), name = 'cortes'),
    path('', HomePagueView.as_view(), name = 'home'),
    
    
]