from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True,  verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500,  blank=True, null=True)
    birthday_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
