import json
from abc import ABC, abstractmethod


class UniversitiesParserCommand(ABC):
    @abstractmethod
    def __call__(self): ...


class UniversitiesParserCommandImpl(UniversitiesParserCommand):
    def __init__(self, universities_repo):
        self.universities_repo = universities_repo

    def __call__(self):
        with open(self._get_file()) as file:
            universities = json.loads(file.read())
        self._split_universities(universities=universities)

    @staticmethod
    def _get_file():
        return 'universities/services/universities_base/universities_base.txt'

    def _split_universities(self, universities):  # TODO maybe bulk create
        for university in universities:
            print(university)  # TODO DELETE
            # TODO Save university


if __name__ == '__main__':  # TODO DELETE
    upc = UniversitiesParserCommandImpl(universities_repo=None)
    upc()
