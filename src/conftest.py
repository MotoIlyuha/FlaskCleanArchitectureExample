import uuid

import pytest


@pytest.fixture
def fixture_profession_developer():
    """ Fixture with Profession example """
    return {
        "profession_id": uuid.uuid4(),
        "name": "Разработчик",
        "description": "Разработчик — это человек, который пишет код программного обеспечения. Этот \
        профессионалу необходимо знать хотя бы один язык программирования."
    }
