from django.contrib import admin
from django.urls import path, include
from controller.list import ListPrograms
from controller.program import ProgramController

ListPrograms.controller = ProgramController
ListPrograms.programs = ProgramController.return_all_programs()
ListPrograms.__close_all__()
ListPrograms.__start_all__()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('program.urls')),
    path('nginx/', include("nginx.urls"))
]


