from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=None)
    subtitle = models.CharField(max_length=400)
    is_published = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    