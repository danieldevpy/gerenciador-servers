from django.db import models

# Create your models here.

class Config(models.Model):
    path = models.CharField(max_length=500)
    user = models.CharField(max_length=100, blank=True)
    status: bool = False

    def __str__(self) -> str:
        return self.path

class Service(models.Model):
    name = models.CharField(max_length=200)
    block = models.TextField()
    active = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return self.name