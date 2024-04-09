from django.shortcuts import redirect, render
from controller.nginx import NginxCommands
from controller.request import RequestCommands
from django.contrib import messages
from settings.models import Config
import os

def get_text(request):
    config = Config.objects.first()
    path = os.path.join(config.path_nginx, 'nginx.conf')
    context = {}
    with open(path, 'r') as arquivo:
        # Lê o conteúdo do arquivo como uma string
        conteudo = arquivo.read()
        context['commands'] = conteudo
        context['lines'] = len(conteudo.split('\n'))//1.5

    return render(request, 'nginx.html', context)

def re_write(request):
    config = Config.objects.first()
    text_nginx = request.POST.get('nginx')
    try:
        NginxCommands.reescrever(text_nginx, config.ubuntu_pass)
        NginxCommands.send_command("restart", config.ubuntu_pass)
        messages.add_message(request, messages.SUCCESS, 'Rewrite success')
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))
    previus_url = RequestCommands.get_previous_url(request)
    if previus_url:
        return redirect(previus_url)
    
    return redirect('/')

