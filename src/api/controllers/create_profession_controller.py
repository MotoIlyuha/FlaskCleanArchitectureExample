from flask import request, jsonify

from src.application.use_cases.create_profession import CreateProfessionUseCase


class CreateProfessionController:
    def __init__(self):
        self.use_case = CreateProfessionUseCase()

    def handle(self):
        data = request.json
        name = data.get('name')
        profession = self.use_case.execute(name)
        return jsonify({"name": profession.name})
