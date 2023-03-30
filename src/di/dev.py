from dependency_injector import containers, providers

from universities import UniversitiesParserCommandImpl
from universities.repo import UniversitiesRepoImpl


class Container(containers.DeclarativeContainer):
    # universities
    universities_repo = providers.Singleton(UniversitiesRepoImpl)

    universities_parser = providers.Singleton(
        UniversitiesParserCommandImpl,
        universities_repo=universities_repo
    )
