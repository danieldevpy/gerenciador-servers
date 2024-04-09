from program.models import Program
from controller.process import ProcessCommands
from settings.models import Config
import subprocess

class GitCommands:

    @classmethod
    def pull(cls, program: Program, force=False):
        path = Config.objects.first().path_programs + program.folder
        command = f'git pull --force'
        _, response = ProcessCommands.start_process(path, command)
        return response.decode('utf-8')
    
    @classmethod
    def reset(cls, program: Program, hash):
        path = Config.objects.first().path_programs + program.folder
        command = f'git reset --hard {hash}'
        _, response = ProcessCommands.start_process(path, command)
        return response.decode('utf-8')

    @classmethod
    def execute_view(cls, comamnd: str, program: Program):
        if comamnd == 'reset':
            return cls.reset(program, 'HEAD')
        elif comamnd == 'pull':
            return cls.pull(program, True)
        else:
            raise Exception("Comando não encontrado")