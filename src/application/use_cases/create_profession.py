from src.domain.interfaces.presenters \
    import CreateProfessionPresenterInterface

from src.domain.entities.profession import Profession
from src.domain.interfaces.profession_repository \
    import ProfessionRepositoryInterface


class CreateProfessionUseCase():
    """ Этот класс отвечает за создание новой профессии.
    """

    def __init__(
            self,
            presenter: CreateProfessionPresenterInterface,
            repository: ProfessionRepositoryInterface
    ):
        self.presenter = presenter
        self.repository = repository

    def execute(self, name: str):
        profession = Profession(name)
        profession.validate()
        # Логика сохранения и другие действия
        return profession
