from controller.processnew import ProcessController
import time

class ListPrograms:

  programs = None
  controller = None
  pages = None

  @classmethod
  def __start_all__(cls):
    if not ListPrograms.programs or not ListPrograms.controller:
      raise Exception("Programas não defindo")
    
    print('Ligando todos os servidores!')

    for program in ListPrograms.programs:
      if program.active:
        if program.status:
          ListPrograms.controller.stop(program)

        process = ProcessController.search_by_port(program.port)
        if process:
          print('kill em', process.pid)
          process.kill()

        if program.sleep:
          time.sleep(program.sleep)

        try:
          ListPrograms.controller.start(program)
        except Exception as e:
          ListPrograms.controller.notification(program, "Erro ao iniciar automaticamente")

  @classmethod
  def __stop_all__(cls):
    if not ListPrograms.programs or not ListPrograms.controller:
      return False
    
    print('Desligando todos os servidores!')

    for program in ListPrograms.programs:
      try:
        ListPrograms.controller.stop(program)
      except:
        pass

  @classmethod
  def get_program_by_id(cls, program_id: int):
    if not ListPrograms.programs or not ListPrograms.controller:
      raise Exception("Programas não defindo")
    for program in ListPrograms.programs:
        if program.id == program_id:
            return program
    return None

  @classmethod
  def get_all(cls):
    if not ListPrograms.programs or not ListPrograms.controller:
      raise Exception("Programas não defindo")
    return ListPrograms.programs
  
  @classmethod
  def check_all(cls):
    if not ListPrograms.programs or not ListPrograms.controller:
      return False

    for program in ListPrograms.programs:
      if program.status and program.process:
        if program.type == "server":
          if not program.process.is_running():
            ListPrograms.controller.crash(program)
            ListPrograms.controller.start(program)
        else:
          if program.process.poll():
            ListPrograms.controller.crash(program)
            ListPrograms.controller.start(program)
