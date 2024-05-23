from dataclasses import dataclass, asdict

from src.domain.value_objects import ProfessionId


@dataclass
class Profession:
    """ Определение сущности профессии
    """
    profession_id: ProfessionId
    name: str
    description: str

    @classmethod
    def from_dict(cls, data):
        """ Преобразование данных из словаря
        """
        return cls(**data)

    def to_dict(self):
        """ Преобразование данных в словарь
        """
        return asdict(self)
