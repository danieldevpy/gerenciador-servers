from django.contrib import admin
from .models import Config
# Register your models here.


class AdminConfig(admin.ModelAdmin):
    pass


admin.site.register(Config, AdminConfig)