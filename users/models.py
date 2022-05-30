from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # kullanıcı silinirse tablodaki verilerde silinmesi için on_delete kullandık. 1-1 dediğimiz için auto id atayacak
    def __str__(self):
        return self.user.username
