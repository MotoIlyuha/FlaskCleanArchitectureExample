""" Module for the CreateProfessionPresenter
"""


from typing import Dict

from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionOutputDto
from src.interactor.interfaces.presenters.create_profession_presenter \
    import CreateProfessionPresenterInterface


class CreateProfessionPresenter(CreateProfessionPresenterInterface):
    """ Класс для CreateProfessionPresenter
    """
    def present(self, output_dto: CreateProfessionOutputDto) -> Dict:
        """ Представляем CreateProfession
        :param output_dto: CreateProfessionOutputDto
        :return: Dict
        """
        return {
            "profession_id": output_dto.profession.profession_id,
            "name": output_dto.profession.name,
            "description": output_dto.profession.description
        }
