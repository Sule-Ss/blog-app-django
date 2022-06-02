from django.urls import path
from .views import home, user_logout, register, user_login, user_profile

urlpatterns = [
    path('', home, name="home"),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    path('login/',user_login,name='user_login'),
    path('profile/',user_profile,name='profile'),
]