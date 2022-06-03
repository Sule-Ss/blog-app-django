from django.contrib import admin

from blogapp.models import Blog, Comment, Favorite

# Register your models here.

admin.site.register(Blog)

admin.site.register(Comment)
admin.site.register(Favorite)