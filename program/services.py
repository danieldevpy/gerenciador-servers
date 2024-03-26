import threading, time, subprocess
from controller.list import ListPrograms


class CheckProgramIsRunning(threading.Thread):
  def __init__(self):
    super().__init__()
    self.stop_event = threading.Event()

  def run(self):
    while not self.stop_event.is_set():
      time.sleep(10)
      programs = ListPrograms.check_all()
      if programs:
        for program in programs:
          try:
            ListPrograms.controller.crash(program)
          except: pass
            
  def stop(self):
      self.stop_event.set()
