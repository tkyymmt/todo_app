from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    #done = models.BooleanField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)