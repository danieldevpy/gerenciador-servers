from django.shortcuts import redirect, render
from controller.nginx import NginxCommands
from .models import Config
from controller.request import RequestCommands
from django.contrib import messages


# Create your views here.

# def get_text(request):
#     services = Service.objects.filter(active=True)
#     context = {'command': NginxCommands.generate_text(services)}
#     return render(request, 'nginx.html', context)

def get_text(request):
    path = Config.objects.first().path
    archive = 'nginx.conf'
    context = {}
    with open(f'{path}/{archive}', 'r') as arquivo:
        # Lê o conteúdo do arquivo como uma string
        conteudo = arquivo.read()
        context['commands'] = conteudo
        context['lines'] = len(conteudo.split('\n'))//1.5

    return render(request, 'nginx.html', context)

def re_write(request):
    text_nginx = request.POST.get('nginx')
    NginxCommands.reescrever(text_nginx, '7890380')
    NginxCommands.send_command("restart", '7890380')
    messages.add_message(request, messages.SUCCESS, 'Rewrite success')
    previus_url = RequestCommands.get_previous_url(request)
    if previus_url:
        return redirect(previus_url)
    
    return redirect('/')


# def re_write(request):
#     services = Service.objects.filter(active=True)
#     try:
#         conf = NginxCommands.generate_text(services)
#         NginxCommands.reescrever(conf, '7890380')
#         NginxCommands.send_command("restart", '7890380')
#         messages.add_message(request, messages.SUCCESS, 'Rewrite success')
#     except Exception as e:
#         messages.add_message(request, messages.ERROR, str(e))

#     previus_url = RequestCommands.get_previous_url(request)
#     if previus_url:
#         return redirect(previus_url)
    
#     return redirect('/')