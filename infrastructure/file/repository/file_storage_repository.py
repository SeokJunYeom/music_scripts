import inject

from settings.config import BaseConfig
from domain.entity.music_entity import MusicEntity
from domain.repository.i_storage_repository import IStorageRepository


class FileStorageRepository(IStorageRepository):

    @inject.autoparams()
    def __init__(self, config: BaseConfig):
        self.config = config

    def save(self, music_entity: MusicEntity):
        path = self.config.FILE_STORAGE_ROOT_DIRECTORY / music_entity.path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            f.write(music_entity.body)
