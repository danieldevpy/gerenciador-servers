import time, os, datetime, psutil, subprocess, shutil
from typing import List
from program.models import Program, Notification, SubProgram
from controller.process import ProcessCommands
from settings.models import Config

class ProgramController:

  @classmethod
  def return_all_programs(cls):
    return Program.objects.all()

  @classmethod
  def start(cls, program: Program) -> str:
      if not program.active:
        raise Exception("Para inicializar o programa deverá estar habilitado")
      # register error  
      try:
        path = os.path.join(Config.objects.first().path_programs, program.folder)
        if program.server:
          process, response = ProcessCommands.start_process(path, program.commands, program.env)
        else:
          commands = f'python -m http.server {program.port}'
          process, response = ProcessCommands.start_process(path, commands, program.env)
        program.status = True
        program.process = process
        program.pid = process.pid
        program.init = datetime.datetime.now()
        program.save()
        sub_programs: List[SubProgram] = program.sub_programs.filter(active=True)
        if sub_programs:
          for sub in sub_programs:
            if sub.sleep:
              time.sleep(sub.sleep)
            try:
              sub_process, _ = ProcessCommands.start_process(path=path, commands=sub.commands, env=sub.env)
              sub.status = True
              sub.process = sub_process
              sub.pid = sub_process.pid
              sub.init = datetime.datetime.now()
              sub.save()
              program.list_programs.append(sub)
            except Exception as e:
              Notification(program=program, desc="Execption ao ligar sub program", error=str(e)).save()
              raise(e)
        return response
      except Exception as e:
        Notification(program=program, desc="Execption ao ligar servidor", error=str(e)).save()
        raise(e)

  @classmethod
  def is_running(cls, program: Program):
    if not program.status or program.process is None:
      return None
    return program.process.poll()
  
  @classmethod
  def crash(cls, program: Program):
    cls.stop(program)
    Notification(program=program, desc="Desligamento inesperado").save()
  
  @classmethod
  def stop(cls, program: Program):
      try:
        parent = psutil.Process(program.process.pid)
        for child in parent.children(recursive=True):
          try:   
            child.terminate()
          except:
            pass
        parent.terminate()
      except:
        pass
      program.status = False
      program.process = None
      program.pid = None
      program.init = None
      program.save()
      sub_programs = program.list_programs
      if sub_programs:
        for sub in sub_programs:
          try:
            sub_parent = psutil.Process(sub.process.pid)
            for child in sub_parent.children(recursive=True):
              try:   
                child.terminate()
              except:
                pass
            sub_parent.terminate()
          except:
            pass
          sub.status = False
          sub.process = None
          sub.pid = None
          sub.init = None
          sub.save()

  @classmethod
  def install_program(cls, program: Program, repository: str, commands: str):
    # Caminho onde o programa será instalado
    base_path = Config.objects.first().path_programs
    destination_path = os.path.join(base_path, program.folder)

    # Comando para clonar o repositório
    clone_command = f'git clone {repository} {destination_path}'
    
    subprocess.run(clone_command, shell=True, check=True, env={})

    if commands:
      ProcessCommands.start_process(path=destination_path, commands=commands)
    
    return True

    
  @classmethod
  def exist_folder(cls, program: Program) -> bool:
    base_path = Config.objects.first().path_programs
    path = os.path.join(base_path, program.folder)
    return os.path.exists(path)
  
  @classmethod
  def remove_folder(cls, program: Program):
      base_path = Config.objects.first().path_programs
      path = os.path.join(base_path, program.folder)
      shutil.rmtree(path)
