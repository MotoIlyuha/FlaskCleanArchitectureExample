""" This module contains the interface for the ProfessionRepository
"""


from abc import ABC, abstractmethod

from src.domain.entities.profession import Profession
from src.domain.value_objects import ProfessionId


class ProfessionRepositoryInterface(ABC):
    """ Этот класс является интерфейсом для ProfessionRepository.
    """

    @abstractmethod
    def get(self, profession_id: ProfessionId) -> Profession:
        """ Получить профессию по идентификатору

        :param profession_id: ProfessionId
        :return: Profession
        """

    @abstractmethod
    def create(self, name: str, description: str) -> Profession:
        """ Создать профессию

        :param name: Profession Name
        :param description: Profession Description
        :return: ProfessionId
        """

    @abstractmethod
    def update(self, profession: Profession) -> Profession:
        """ Сохранить профессию

        :param Profession: Profession
        :return: Profession
        """
