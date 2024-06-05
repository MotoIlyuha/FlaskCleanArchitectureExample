from abc import ABC, abstractmethod


class CliMemoryControllerInterface(ABC):
    @abstractmethod
    def execute(self):
        """ Executes the controller
        """
