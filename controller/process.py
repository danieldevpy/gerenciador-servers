import subprocess, shutil
from typing import Tuple

class ProcessCommands:

    @classmethod
    def start_process(cls, path: str, commands: str, env = False) -> Tuple[subprocess.Popen, str]:
        command = ['bash', '-c', commands]
        if env:
          process = subprocess.Popen(command, cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env={})
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
      processo = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      return processo