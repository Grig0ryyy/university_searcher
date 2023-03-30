import json
from abc import ABC, abstractmethod

from src.universities.models import University


class UniversitiesParserCommand(ABC):
    @abstractmethod
    def __call__(self): ...


class UniversitiesParserCommandImpl(UniversitiesParserCommand):
    def __init__(self, universities_repo):
        self.universities_repo = universities_repo

    def __call__(self):
        with open(self._get_file()) as file:
            universities = json.loads(file.read())
        self._split_universities(universities_data=universities)

    @staticmethod
    def _get_file():
        return 'universities/services/universities_base/universities_base.txt'  # TODO mb env

    def _split_universities(self, universities_data):
        universities = [
            University(
                name=university_data['name'],
                country=university_data['country'],
                alpha_two_code=university_data['alpha_two_code'],
                web_page=university_data['web_pages'][0] if university_data['web_pages'] else None
            )
            for university_data in universities_data
        ]

        self.universities_repo.bulk_create(universities)
