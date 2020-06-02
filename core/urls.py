from django.urls import path
from .views import home, login, Register

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', Register.as_view(), name="register")
]
