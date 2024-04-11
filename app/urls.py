from django.contrib import admin
from django.urls import path, include
from controller.list import ListPrograms
from controller.program import ProgramController
from threading import Thread
ListPrograms.controller = ProgramController
ListPrograms.programs = ProgramController.return_all_programs()
Thread(target=ListPrograms.__start_all__).start()



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('program.urls')),
    path('nginx/', include("nginx.urls"))
]


