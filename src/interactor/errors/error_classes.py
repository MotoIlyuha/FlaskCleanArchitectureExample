class FieldValueNotPermittedException(Exception):
    """ Исключение возникает, когда поле пусто"""

    def __init__(self, field_name: str, field_value: str) -> None:
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self) -> str:
        return f"{self.field_name.capitalize()}: {self.field_value} is not \
permitted"
