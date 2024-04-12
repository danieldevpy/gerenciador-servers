from django.db import models
from datetime import datetime

class Config(models.Model):
    name = models.CharField(max_length=200)
    ubuntu_pass = models.CharField(max_length=200)
    ip_server = models.CharField(max_length=200, blank=True, null=True)
    path_nginx = models.CharField(max_length=500)
    path_programs = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
    

class NginxBackup(models.Model):
    date = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    content = models.TextField()