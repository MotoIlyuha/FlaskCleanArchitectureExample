from abc import ABC, abstractmethod


class CliMemoryControllerInterface(ABC):
    """ Этот класс является интерфейсом для класса CliMemoryController.
    """
    @abstractmethod
    def execute(self):
        """ Выполняет контроллер
        """
