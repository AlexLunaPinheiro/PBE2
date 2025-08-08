from django.urls import path
from .views import LivroListCreate, LivroRetrieveUpdateDestroy, AutorListCreate, AutorRetrieveUpdateDestroy

urlpatterns = [
    path('livros/', LivroListCreate.as_view()),
    path('livros/<int:pk>/',LivroRetrieveUpdateDestroy.as_view()),
    path('autor/',AutorListCreate.as_view()),
    path('autor/<int:pk>',AutorRetrieveUpdateDestroy.as_view())
    
]
