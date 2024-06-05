import sys

from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import CliMemoryControllerInterface


class ExitController(CliMemoryControllerInterface):
    def execute(self):
        print("Exiting the program")
        sys.exit()
