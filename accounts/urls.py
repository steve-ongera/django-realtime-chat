from django.urls import path

from .views import home, user_login, user_logout, user_register

app_name = "accounts"

urlpatterns = [
    path("", home, name="home"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]
