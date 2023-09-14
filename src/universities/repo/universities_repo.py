from abc import ABC, abstractmethod
from typing import List
from django.db.models import QuerySet

from universities.models import University
from universities.services.repo import UniversitiesRepo


class UniversitiesRepoImpl(UniversitiesRepo):

    def bulk_create(self, universities_data: List) -> QuerySet[University]:
        universities = [
            University(
                name=university_data['name'],
                country=university_data['country'],
                alpha_two_code=university_data['alpha_two_code'],
                web_page=university_data['web_pages'][0] if university_data['web_pages'] else None
            )
            for university_data in universities_data
        ]
        return University.objects.bulk_create(universities)
