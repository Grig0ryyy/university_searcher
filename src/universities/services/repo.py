from abc import ABC, abstractmethod
from typing import List


class UniversitiesRepo(ABC):
    @abstractmethod
    def bulk_create(self, universities_data: List): ...
