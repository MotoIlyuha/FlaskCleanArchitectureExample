from typing import Dict

from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionOutputDto
from src.interactor.interfaces.presenters.create_profession_presenter \
    import CreateProfessionPresenterInterface


class CreateProfessionPresenter(CreateProfessionPresenterInterface):

    def present(self, output_dto: CreateProfessionOutputDto) -> Dict:
        return {
            "profession_id": output_dto.profession.profession_id,
            "name": output_dto.profession.name,
            "description": output_dto.profession.description
        }
