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
      if program.status:
        ListPrograms.controller.stop(program)
        time.sleep(1)

      if program.sleep: time.sleep(program.sleep)
      try:
        ListPrograms.controller.start(program)
      except: pass

  @classmethod
  def __close_all__(cls):
    if not ListPrograms.programs or not ListPrograms.controller:
      return False
    
    for program in ListPrograms.programs:
      try:
        ListPrograms.controller.find_and_kill_process(program.port)
      except:
        pass


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
    
    p = []

    for program in ListPrograms.programs:
      if program.status:
        response = ListPrograms.controller.is_running(program)
        if response:
          p.append(program)

    return p
