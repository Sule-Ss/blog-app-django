from .views import blog_delete, home, blog_list, blog_detail,blog_add,blog_update,blog_delete
from django.urls import path

urlpatterns = [
     path('', home, name="home"),
     path('add/', blog_add, name="add"),
     path('list/', blog_list, name="list"),
     path('detail/<int:id>/', blog_detail, name="detail"),
     path('update/<int:id>/', blog_update, name="update"),
     path('delete/<int:id>/', blog_delete, name="delete"),
]