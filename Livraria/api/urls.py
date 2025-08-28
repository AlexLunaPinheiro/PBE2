from django.urls import path
from .views import AutorView, LivroView, EditoraView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('autor/', AutorView.as_view()),
    path('autor/<int:pk>',AutorView.as_view()),

    path('livro/',LivroView.as_view()),
    path('livro/<int:pk>',LivroView.as_view()),

    path('editora/',EditoraView.as_view()),
    path('editora/<int:pk>',EditoraView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
