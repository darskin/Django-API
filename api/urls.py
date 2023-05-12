from django.urls import path
from .views import *

urlpatterns = [
    path("articulos/", articuloView.as_view(), name="articulos_lista"),
    path("articulos/<int:id>", articuloView.as_view(), name="articulos_procesados"),
    path("pedidos/", pedidoView.as_view(), name="pedidos_lista"),  
    path("pedidos/<int:id>", pedidoView.as_view(), name="pedidos_procesados"),
    ]
