from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField()
