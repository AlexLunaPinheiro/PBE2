from django.urls import path
from . import views

urlpatterns = [
    path("listar-bibliotecarios",views.ListarBibliotecario.as_view(),name="listar-bibliotecarios")
]


