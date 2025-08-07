from django.urls import path
from .views import LivroListCreate, LivroRetrieve, AutorListCreate

urlpatterns = [
    path('livros/', LivroListCreate.as_view()),
    path('autor/',AutorListCreate.as_view()),
    path('livros/<int:pk>/',LivroRetrieve.as_view()),

]