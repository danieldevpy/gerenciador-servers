from django.apps import AppConfig
from .services import CheckProgramIsRunning
import signal


config = False

if not config:

    check = CheckProgramIsRunning()

    class ProgramConfig(AppConfig):

        default_auto_field = 'django.db.models.BigAutoField'
        name = 'program'

        def shutdown_handler(self, signum, frame):
            check.stop()
            exit(0)

        def ready(self) -> None:
            signal.signal(signal.SIGINT, self.shutdown_handler)
            check.start()
