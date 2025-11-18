from django.db import models
from datetime import datetime
# Create your models here.
class Job(models.Model):
    name=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name