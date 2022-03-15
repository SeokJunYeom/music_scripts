from domain.entity.music_entity import MusicEntity
from domain.repository.i_storage_repository import IStorageRepository


class FileStorageRepository(IStorageRepository):

    def save(self, music_entity: MusicEntity):
        pass
