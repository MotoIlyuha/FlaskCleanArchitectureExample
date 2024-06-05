from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import CliMemoryControllerInterface
from src.infra.repositories.profession_in_memory_repository \
    import ProfessionInMemoryRepository
from src.interactor.dtos.create_profession_dtos import CreateProfessionInputDto
from src.interactor.use_cases.create_profession import CreateProfessionUseCase
from ..presenters.create_profession_presenter import CreateProfessionPresenter
from ..views.create_profession_view import CreateProfessionView


def _get_profession_info() -> CreateProfessionInputDto:
    name = input("Enter the profession name:")
    description = input("Enter the profession description:")
    return CreateProfessionInputDto(name, description)


class CreateProfessionController(CliMemoryControllerInterface):

    def execute(self):
        repository = ProfessionInMemoryRepository()
        presenter = CreateProfessionPresenter()
        input_dto = _get_profession_info()
        use_case = CreateProfessionUseCase(presenter, repository)
        result = use_case.execute(input_dto)
        view = CreateProfessionView()
        view.show(result)
