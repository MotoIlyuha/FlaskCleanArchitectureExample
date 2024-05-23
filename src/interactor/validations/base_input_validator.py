from typing import Dict

from cerberus import Validator  # type: ignore


class BaseInputValidator:
    """ Этот класс предоставляет базовый класс для проверки ввода.
    """

    def __init__(self, data: Dict[str, str]):
        self.data = data
        self.errors: Dict = {}

    def verify(self, schema: Dict) -> None:
        """ Проверяет входные данные на соответствие предоставленной схеме.
        :param schema: Схема для проверки
        :return: None
        :raises ValueError: Если входные данные недействительны.
        """
        validator = Validator(schema)
        if not validator.validate(self.data):
            self.errors = validator.errors
            self._raise_validation_error()

    def _raise_validation_error(self):
        error_messages = []
        for field, messages in self.errors.items():
            for message in messages:
                error_messages.append(f"{field.capitalize()}: {message}")
        raise ValueError("\n{}".join(error_messages))
