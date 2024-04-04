import subprocess, shutil
from typing import Tuple
import os

class ProcessCommands:

    @classmethod
    def start_process(cls, path: str, commands: str, env = False) -> Tuple[subprocess.Popen, str]:
        command = ['bash', '-c', commands]

        if env:
          process = subprocess.Popen(command, cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env={
                'PATH':  os.environ['PATH']
          })
        else:
          process = subprocess.Popen(command, cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  
        try:
            response, error = process.communicate(timeout=5)
            if error:
                raise Exception(error)
        except subprocess.TimeoutExpired:
           response = 'Não foi possivel obter a resposta do processo'

        return process, response
    
    @classmethod
    def execute_command_shell(cls, command):
      processo = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env={})
      return processo
    
    @classmethod
    def get_pid_listening_port(cls, port):
      try:
          # Executar o comando para listar os processos que estão escutando na porta específica
          command_output = subprocess.check_output(['lsof', '-t', '-i', f'tcp:{port}'])
          # Dividir a saída em linhas e converter para lista de PID
          pid_list = command_output.decode().strip().split('\n')[0]
          return pid_list
      except subprocess.CalledProcessError:
          # Se nenhum processo estiver escutando na porta, retornar uma lista vazia
          return 0