

config = True

if not config:
    from django.apps import AppConfig
    from .services import CheckProgramIsRunning
    from controller.list import ListPrograms
    import signal

    check = CheckProgramIsRunning()

    class ProgramConfig(AppConfig):

        default_auto_field = 'django.db.models.BigAutoField'
        name = 'program'

        def shutdown_handler(self, signum, frame):
            check.stop()
            ListPrograms.__stop_all__()
            exit(0)


        def ready(self) -> None:
            signal.signal(signal.SIGINT, self.shutdown_handler)
            check.start()
