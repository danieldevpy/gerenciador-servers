from django.db import models

# Create your models here.

class Config(models.Model):
    path = models.CharField(max_length=500)
    user = models.CharField(max_length=100, blank=True)
    status: bool = False

    def __str__(self) -> str:
        return self.path

