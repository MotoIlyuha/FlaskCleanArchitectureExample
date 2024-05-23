from abc import ABC, abstractmethod
from typing import Dict

from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionOutputDto


class CreateProfessionPresenterInterface(ABC):
    """ Класс интерфейса ProfessionPresenter
    """
    @abstractmethod
    def present(self, output_dto: CreateProfessionOutputDto) -> Dict:
        """ Представьте профессию
        """
