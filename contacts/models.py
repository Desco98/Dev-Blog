from django.db import models
from datetime import datetime

class Contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=None)
    sent_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name