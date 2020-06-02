from django.urls import path
from .views import home, Register

urlpatterns = [
    path('', home, name="home"),
    path('register/', Register.as_view(), name="register")
]
