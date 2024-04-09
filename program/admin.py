from django.contrib import admin
from .models import Program, Notification, SubProgram

# Register your models here.

class ProgramAdmin(admin.ModelAdmin):
    pass

class NotificationAdmin(admin.ModelAdmin):
    pass

class SubProgramAdmin(admin.ModelAdmin):
    pass

admin.site.register(Program, ProgramAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(SubProgram, SubProgramAdmin)