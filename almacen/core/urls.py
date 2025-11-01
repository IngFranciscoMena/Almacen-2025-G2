from django.urls import path

from .views import CustomLoginView, CustomLogoutView, RegistroUsuarioCreateView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('register/', RegistroUsuarioCreateView.as_view(), name="register")
]