import subprocess, datetime
from typing import Optional
from django.db import models
from django.utils import timezone


class Program(models.Model):
    name = models.CharField(max_length=200)
    folder = models.CharField(max_length=200, null=True, blank=True)
    port = models.IntegerField()
    commands = models.CharField(max_length=500)
    desc = models.CharField(max_length=200, null=True, blank=True)
    sleep = models.IntegerField(default=1, null=True)
    password = models.BooleanField(default=False, null=True)
    status = models.BooleanField(default=False, null=True)
    active = models.BooleanField(default=False, null=True)
    type = models.CharField(max_length=100, choices=(("server", "Servidor"), ("service", "Serviço"), ('page', 'Pagina Estatica')))

    process: Optional[subprocess.Popen] = None
    pid: int = None
    init: datetime.datetime = None
    list_programs = []

    def __str__(self) -> str:
        return self.name


class SubProgram(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='sub_programs')
    name = models.CharField(max_length=200)
    sleep = models.IntegerField(default=0, null=True)
    status = models.BooleanField(default=False, null=True)
    active = models.BooleanField(default=False, null=True)
    env = models.BooleanField(default=False, null=True)
    commands = models.CharField(max_length=500)
    
    process: Optional[subprocess.Popen] = None
    pid: int = None
    init: datetime.datetime = None

    def __str__(self) -> str:
        return self.name


class Notification(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200, null=True, blank=True)
    error = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    checked = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return f'{self.desc}/{self.program.name}'