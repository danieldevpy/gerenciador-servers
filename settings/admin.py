from django.contrib import admin
from .models import Config, NginxBackup
# Register your models here.


class AdminConfig(admin.ModelAdmin):
    pass


class AdminNginxBakcup(admin.ModelAdmin):
    pass


admin.site.register(Config, AdminConfig)
admin.site.register(NginxBackup, AdminNginxBakcup)