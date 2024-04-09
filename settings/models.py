from django.db import models

# Create your models here.


class Config(models.Model):
    name = models.CharField(max_length=200)
    ubuntu_pass = models.CharField(max_length=200)
    path_nginx = models.CharField(max_length=500)
    path_programs = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name