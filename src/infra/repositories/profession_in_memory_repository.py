import copy
import uuid
from typing import Dict

from src.domain.entities.profession import Profession
from src.domain.interfaces.profession_repository \
    import ProfessionRepositoryInterface
from src.domain.value_objects import ProfessionId


class ProfessionInMemoryRepository(ProfessionRepositoryInterface):
    """ Репозиторий InMemory для профессий
    """
    def __init__(self) -> None:
        self._data: Dict[ProfessionId, Profession] = {}
        self.professions = []

    def get(self, profession_id: ProfessionId) -> Profession:
        """ Получить профессию по идентификатору

        :param profession_id: ProfessionId
        :return: Profession
        """
        return copy.deepcopy(self._data[profession_id])

    def save(self, profession: Profession):
        self.professions.append(profession)

    def create(self, name: str, description: str) -> Profession:
        profession = Profession(
            profession_id=uuid.uuid4(),
            name=name,
            description=description
        )
        self._data[profession.profession_id] = copy.deepcopy(profession)
        return copy.deepcopy(self._data[profession.profession_id])

    def update(self, profession: Profession) -> Profession:
        self._data[profession.profession_id] = copy.deepcopy(profession)
        return copy.deepcopy(self._data[profession.profession_id])
