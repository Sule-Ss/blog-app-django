from .views import about, blog_delete, home, blog_list, blog_detail,blog_add,blog_update,blog_delete
from django.urls import path

urlpatterns = [
     path('', home, name="home"),
     path('about/', about, name="about"),
     path('detail/<slug:slug>/', blog_detail, name="detail"),
     path('add/', blog_add, name="add"),
     path('list/', blog_list, name="list"),
     path('update/<slug:slug>/', blog_update, name="update"),
     path('delete/<slug:slug>/', blog_delete, name="delete"),
]