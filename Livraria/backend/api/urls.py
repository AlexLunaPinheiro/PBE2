from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.auth_views import RegisterViewSet
from api.views.autores_views import AutorView
from api.views.editora_views import EditoraView
from api.views.livro_views import LivroView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'registro',RegisterViewSet, basename='registro')
urlpatterns = [
    path('autores/', AutorView.as_view()),
    path('autores/<int:pk>',AutorView.as_view()),

    path('livros/',LivroView.as_view()),
    path('livros/<int:pk>',LivroView.as_view()),

    path('editoras/',EditoraView.as_view()),
    path('editoras/<int:pk>',EditoraView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('',include(router.urls))
]
