import json
from abc import ABC, abstractmethod

from universities.services.repo import UniversitiesRepo


class UniversitiesParserCommand(ABC):
    @abstractmethod
    def __call__(self): ...


class UniversitiesParserCommandImpl(UniversitiesParserCommand):
    def __init__(self, universities_repo: UniversitiesRepo):
        self.universities_repo = universities_repo

    def __call__(self):
        with open(self._get_file()) as file:
            universities = json.loads(file.read())
        self._create_universities(universities_data=universities)

    @staticmethod
    def _get_file():
        return 'universities/services/universities_base/universities_base.txt'  # TODO mb env

    def _create_universities(self, universities_data):
        self.universities_repo.bulk_create(universities_data=universities_data)
