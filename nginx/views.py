from django.shortcuts import redirect
from controller.nginx import NginxCommands
from .models import Service
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def get_text(request):
    services = Service.objects.filter(active=True)
    return HttpResponse(NginxCommands.generate_text(services), content_type='text/plain')

def re_write(request):
    services = Service.objects.filter(active=True)
    try:
        conf = NginxCommands.generate_text(services)
        NginxCommands.reescrever(conf, "devpython")
        NginxCommands.send_command("restart", "devpython")
        messages.add_message(request, messages.SUCCESS, 'Rewrite success')
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))

    return redirect('/')
