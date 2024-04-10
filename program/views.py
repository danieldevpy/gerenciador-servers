from django.shortcuts import render, redirect
from controller.list import ListPrograms
from controller.program import ProgramController
from controller.git import GitCommands
from controller.request import RequestCommands
from program.models import Notification, Program
from django.contrib import messages
from settings.models import Config


def index(request):
    config = Config.objects.first()
    programs = ListPrograms.get_all()
    programs_enable = [program for program in programs if program.active]
    programs_disabled = [program for program in programs if not program.active]

    context = {
        'programs_enable': programs_enable,
        'programs_disabled': programs_disabled,
        'ip': config.ip_server
    }
    return render(request, 'index.html', implement_context(context))

def detail(request, pk):
    program = ListPrograms.get_program_by_id(pk)
    if not program:
        messages.add_message(request, messages.ERROR, 'Servidor não encontrado')
        return redirect('/')
    
    installed = ProgramController.exist_folder(program)
    notifys = Notification.objects.filter(program=program).order_by('-id')
    sub_programs = program.sub_programs.all()

    context = {
        'program': program,
        'installed': installed,
        'notifys': notifys,
        'sub_programs': sub_programs
    }
    return render(request, 'detail.html', implement_context(context))

def reload(request):
    ListPrograms.programs = ProgramController.return_all_programs()
    messages.add_message(request, messages.SUCCESS, 'Reload')
    return redirect('/')

def stop_all(request):
    ListPrograms.__stop_all__()
    messages.add_message(request, messages.SUCCESS, 'Stopped')
    return redirect('/')

def start(request, pk):
    program = ListPrograms.get_program_by_id(pk)
    if not program:
        messages.add_message(request, messages.ERROR, 'Servidor não encontrado')
        return redirect('/')
    try:
        response = ProgramController.start(program)
        messages.add_message(request, messages.SUCCESS, response)
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))

    return redirect(f'/detail/{pk}')

def stop(request, pk):
    program = ListPrograms.get_program_by_id(pk)
    if not program:
        messages.add_message(request, messages.ERROR, 'Servidor não encontrado')
        return redirect('/')
    try:
        ProgramController.stop(program)
        messages.add_message(request, messages.SUCCESS, 'Servidor desligado.')
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))
    return redirect(f'/detail/{pk}')

def install(request, pk):
    program = Program.objects.get(pk=pk)
    if not program:
        messages.add_message(request, messages.ERROR, 'Servidor não encontrado')
        return redirect('/')
    repo = request.POST.get('repository_url').lower()
    repository_url = f'https://github.com/{repo}' 
    commands = request.POST.get('commands')
    try:
        ProgramController.install_program(program, repository_url, commands)
        messages.add_message(request, messages.SUCCESS, 'Servidor Instalado!')
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))

    previus_url = RequestCommands.get_previous_url(request)
    if previus_url:
        return redirect(previus_url)
    
    return redirect('/')

def uninstall(request, pk):
    program = Program.objects.get(pk=pk)
    if not program:
        messages.add_message(request, messages.ERROR, 'Servidor não encontrado')
        return redirect('/')
    try:
        ProgramController.remove_folder(program)
        messages.add_message(request, messages.SUCCESS, 'Servidor Desinstalado!')
    except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
   
    previus_url = RequestCommands.get_previous_url(request)
    if previus_url:
        return redirect(previus_url)
    
    return redirect('/')

def git(request, command, pk):
    program = Program.objects.get(pk=pk)
    if not program:
        messages.add_message(request, messages.ERROR, 'Servidor não encontrado')
        return redirect('/')
    try:
        response = GitCommands.execute_view(command, program)
        print(response)
        messages.add_message(request, messages.SUCCESS, response)
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))

    previus_url = RequestCommands.get_previous_url(request)
    if previus_url:
        return redirect(previus_url)
    
    return redirect('/')

def remove_notification(request, pk):
    try:
        notification = Notification.objects.get(pk=pk)
        notification.delete()
        messages.add_message(request, messages.SUCCESS, 'Notificação deletada com sucesso!')
    except Exception as e:
        messages.add_message(request, messages.ERROR, str(e))

    previus_url = RequestCommands.get_previous_url(request)
    if previus_url:
        return redirect(previus_url)
    return redirect('/')

def implement_context(context: dict):
    context['notifications'] = Notification.objects.filter(checked=False)
    return context