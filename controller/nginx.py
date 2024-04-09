
from typing import List
import os, tempfile
from controller.process import ProcessCommands
from settings.models import Config


class NginxCommands:
    
    @classmethod
    def reescrever(cls, nginx_conf: str, password):
        config = Config.objects.first()

        path = config.path_nginx
        nginx_path = os.path.join(path, 'nginx.conf')

        commmand_remove = f"echo {password} | sudo -S rm -rf {path}/nginx.conf"
        process_remove = ProcessCommands.execute_command_shell(commmand_remove)
        saida, erro = process_remove.communicate(timeout=15)

        arquivo_temporario = tempfile.NamedTemporaryFile(mode='w', delete=False)
        arquivo_temporario.write(nginx_conf)

        command_move = f"echo {password} | sudo -S mv {arquivo_temporario.name} {nginx_path}"
        process_move = ProcessCommands.execute_command_shell(command_move)
        saida, erro = process_move.communicate(timeout=15)

    @classmethod
    def send_command(cls, command, password=False):
        if password:
            comando = f"echo {password} | sudo -S systemctl {command} nginx"
        else:
            comando = f"sudo -S systemctl {command} nginx"

        process = ProcessCommands.execute_command_shell(comando)
        saida, erro = process.communicate(timeout=3)  # Aguarda a finalização do processo

        if process.returncode == 0:
            return saida, erro
        else:
            raise Exception(erro)
        
    