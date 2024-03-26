from django.contrib import admin
from . models import Config, Service
# Register your models here.


class AdminConfig(admin.ModelAdmin):
    pass


class AdminService(admin.ModelAdmin):
    pass

admin.site.register(Config, AdminConfig)
admin.site.register(Service, AdminService)