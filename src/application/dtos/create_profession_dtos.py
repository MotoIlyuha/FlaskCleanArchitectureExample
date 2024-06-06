from dataclasses import dataclass, asdict

from src.domain.entities.profession import Profession


@dataclass
class CreateProfessionInputDto:
    """ Введите Dto для создания профессии """
    name: str
    description: str

    def to_dict(self):
        """ Преобразование данных в словарь
        """
        return asdict(self)


@dataclass
class CreateProfessionOutputDto:
    """ Вывод Dto для создания профессии"""
    profession: Profession
