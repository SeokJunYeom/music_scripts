import abc
from typing import Generator

from domain.entity.music_entity import MusicEntity


class IBackupRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_all(self, musics: Generator[MusicEntity, None, None]):
        raise NotImplemented
