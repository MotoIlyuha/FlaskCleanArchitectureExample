from typing import Dict

from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionInputDto, CreateProfessionOutputDto
from src.interactor.interfaces.presenters.create_profession_presenter \
    import CreateProfessionPresenterInterface
from src.interactor.interfaces.repositories.profession_repository \
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

    def execute(
            self,
            input_dto: CreateProfessionInputDto
    ) -> Dict:
        """ Этот метод отвечает за создание новой профессии.
        :param input_dto: Объект передачи входных данных.
        :type input_dto: CreateProfessionInputDto
        :return: Dict
        """

        profession = self.repository.create(
            input_dto.name,
            input_dto.description
        )
        output_dto = CreateProfessionOutputDto(profession)
        return self.presenter.present(output_dto)
