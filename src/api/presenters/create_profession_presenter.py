""" Module for the CreateProfessionPresenter
"""


from typing import Dict

from src.domain.interfaces.presenters \
    import CreateProfessionPresenterInterface

from src.application.dtos.create_profession_dtos \
    import CreateProfessionOutputDto


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
