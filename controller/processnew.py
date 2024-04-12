import psutil, time, subprocess, os
from subprocess import Popen
from psutil import Process


class ProcessController:

    @classmethod
    def start_process(cls, path:str, command: str, password = False, error = True) -> Popen:
        if password:
            command = f'echo {password} | ' + command
        cmd = ['bash', '-c', command]

        process = subprocess.Popen(cmd, cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env={
        'PATH':  os.environ['PATH']
          })
        if not error:
            return process
        try:
            return_code = process.wait(timeout=10)
            if return_code == 0:
                return Process
            else:
                stdout, stderr = process.communicate(timeout=5)
       
                if stderr:
                    raise Exception(stderr.decode())
                elif stdout:
                    raise Exception(stdout.decode())
        except: pass
       
    @classmethod
    def start_program(cls, path: str, commands: str, port: int) -> Process:

        cls.start_process(path, commands)
        secondy_process = cls.get_process(port)

        if not secondy_process:
            
            raise Exception("Não foi possivel achar o pid")
        
        return secondy_process

    @classmethod
    def search_by_port(cls, port):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                connections = proc.connections()
                for conn in connections:
                    if conn.laddr.port == port:
                        return proc 
            except psutil.AccessDenied:
                pass

        return False
    
    @classmethod
    def get_process(cls, port, attemps=5):
        for _ in range(attemps):
            process = cls.search_by_port(port)
            if process:
                return process
            time.sleep(1)
            
        return False